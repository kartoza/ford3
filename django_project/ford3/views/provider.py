from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import transaction, IntegrityError
from django.db.models import F
from ford3.forms.provider_form import ProviderForm
from ford3.models import (
    Campus,
    Provider,
)


@transaction.atomic
def edit_provider(request, provider_id):
    if request.method == 'POST':
        # upload button is pressed
        if 'upload_logo' in request.POST:
            form = ProviderForm(request.POST, request.FILES)
            # users press upload button without specifying a file
            if not request.FILES:
                context = {
                    'form': form,
                    'provider_id': provider_id,
                }
                return render(request, 'provider_form.html', context)

            uploaded_file = request.FILES['file_logo']
            fs = FileSystemStorage()
            logo_name = fs.save(uploaded_file.name, uploaded_file)
            logo_url = os.path.join(settings.MEDIA_URL, logo_name)

            provider = get_object_or_404(
                Provider,
                id=provider_id
            )

            provider.provider_logo = logo_url
            provider.save()

            context = {
                'form': form,
                'provider_id': provider_id,
                'provider_logo': logo_url,

            }
            return render(request, 'provider_form.html', context)
        # Submit button is pressed
        else:
            form = ProviderForm(request.POST)
            if form.is_valid():
                new_provider = Provider.objects.filter(pk=provider_id).first()
                provider_type = form.cleaned_data['provider_type']
                telephone = form.cleaned_data['telephone']
                email = form.cleaned_data['email']
                physical_address_line_1 = (
                    form.cleaned_data['physical_address_line_1'])
                physical_address_line_2 = (
                    form.cleaned_data['physical_address_line_2'])
                physical_address_city = form.cleaned_data['physical_address_city']
                postal_address = form.cleaned_data['postal_address']
                admissions_contact_no = form.cleaned_data['admissions_contact_no']
                new_provider.provider_type = provider_type
                new_provider.telephone = telephone
                new_provider.email = email
                new_provider.physical_address_line_1 = physical_address_line_1
                new_provider.physical_address_line_2 = physical_address_line_2
                new_provider.physical_address_city = physical_address_city
                new_provider.postal_address = postal_address
                new_provider.admissions_contact_no = admissions_contact_no
                new_provider.save()
                campus_list = request.POST.getlist('campus_name')
                number_of_campuses = len(campus_list)
                try:
                    with transaction.atomic():
                        for idx in range(number_of_campuses):
                            campus_name = campus_list[idx]
                            Campus.objects.create(provider=new_provider,
                                                  name=campus_name)
                except IntegrityError:
                    return render(request, 'provider_form.html', {'form': form})
                redirect_url = '/providers/' + str(new_provider.id)
                return redirect(redirect_url)
    else:
        provider = get_object_or_404(
            Provider,
            id=provider_id
        )
        form = ProviderForm(instance=provider)
        context = {
            'form': form,
            'provider_id': provider_id,
            'is_new_provider': provider.is_new_provider,
            'provider_logo': provider.provider_logo,
        }
        return render(request, 'provider_form.html', context)


def show_provider(request, provider_id):
    context = {}
    form_data = {}
    campus_query = Campus.objects.filter(provider__id=provider_id).annotate(
        campus_name=F('name'),
        campus_id=F('id'),
        provider_name=F('provider__name')
    )
    campus_data = campus_query.values('name', 'id')
    provider_name = campus_query.values('provider_name')[0]['provider_name']

    form_data['campus_list'] = list(campus_data)
    form_data['provider_name'] = str(provider_name)

    context['form_data'] = form_data
    context['provider'] = {
        'campus': campus_data,
        'id': provider_id
    }
    return render(request, 'provider.html', context)
