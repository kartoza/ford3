from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.db import transaction, IntegrityError
from django.urls import reverse
from ford3.forms.provider_form import ProviderForm
from ford3.models import (
    Campus,
    Provider,
)


@transaction.atomic
def edit_provider(request, provider_id):
    if request.method == 'POST':
        form = ProviderForm(request.POST, request.FILES)
        if form.is_valid():
            new_provider = Provider.objects.filter(pk=provider_id).first()
            provider_type = form.cleaned_data['provider_type']
            telephone = form.cleaned_data['telephone']
            email = form.cleaned_data['email']
            physical_address_line_1 = (
                form.cleaned_data['physical_address_line_1'])
            physical_address_line_2 = (
                form.cleaned_data['physical_address_line_2'])
            physical_address_city = (
                form.cleaned_data['physical_address_city'])
            postal_address_differs = (
                form.cleaned_data['postal_address_differs'])
            physical_address_postal_code = (
                form.cleaned_data['physical_address_postal_code'])
            postal_address_line_1 = (
                form.cleaned_data['postal_address_line_1'])
            postal_address_line_2 = (
                form.cleaned_data['postal_address_line_2'])
            postal_address_city = form.cleaned_data['postal_address_city']
            postal_address_postal_code = (
                form.cleaned_data['postal_address_postal_code'])
            admissions_contact_no = (
                form.cleaned_data['admissions_contact_no'])
            provider_logo = form.cleaned_data['provider_logo']
            # use case: user does not upload logo, then use old logo
            if not form.cleaned_data['provider_logo']:
                provider_logo = new_provider.provider_logo
            new_provider.provider_type = provider_type
            new_provider.telephone = telephone
            new_provider.email = email
            new_provider.physical_address_line_1 = physical_address_line_1
            new_provider.physical_address_line_2 = physical_address_line_2
            new_provider.physical_address_city = physical_address_city
            new_provider.physical_address_postal_code = (
                physical_address_postal_code)
            new_provider.postal_address_differs = postal_address_differs
            if postal_address_differs:
                new_provider.postal_address_line_1 = postal_address_line_1
                new_provider.postal_address_line_2 = postal_address_line_2
                new_provider.postal_address_city = postal_address_city
                new_provider.postal_address_postal_code = (
                    postal_address_postal_code)
            else:
                new_provider.postal_address_line_1 = physical_address_line_1
                new_provider.postal_address_line_2 = physical_address_line_2
                new_provider.postal_address_city = physical_address_city
                new_provider.postal_address_postal_code = (
                    physical_address_postal_code)
            new_provider.admissiofns_contact_no = admissions_contact_no
            new_provider.provider_logo = provider_logo
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
            redirect_url = reverse(
                'show-provider',
                args=[str(new_provider.id)])
            return redirect(redirect_url)
        # form is not valid
        else:
            provider = Provider.objects.filter(pk=provider_id).first()
            # use uploaded logo if form submission failed
            if form.cleaned_data['provider_logo']:
                form.instance.provider_logo = \
                    form.cleaned_data['provider_logo']
            # otherwise, use old logo
            else:
                form.instance.provider_logo = provider.provider_logo

            context = {
                'form': form,
                'provider_id': provider_id,
                'provider': provider,
                'is_new_provider': provider.is_new_provider

            }
            return render(request, 'provider_form.html', context)
    else:
        provider = get_object_or_404(
            Provider,
            id=provider_id
        )
        form = ProviderForm(instance=provider)
        context = {
            'form': form,
            'provider_id': provider_id,
            'provider': provider,
            'is_new_provider': provider.is_new_provider,
        }

        return render(request, 'provider_form.html', context)


def show_provider(request, provider_id):
        provider = get_object_or_404(
            Provider,
            id=provider_id
        )
        if provider.is_new_provider:
            redirect_url = reverse(
                'edit-provider',
                args=[str(provider.id)])
            return redirect(redirect_url)

        context = {
            'provider': provider
        }
        context['campus_error'] = ''
        if request.method == 'POST':
            new_campus_name = str(request.POST['add_campus_input_name'])
            campus_query = (Campus.objects.filter(
                provider__id=provider.id,
                name=new_campus_name).count())
            if campus_query == 0:
                new_campus_object = Campus()
                new_campus_object.name = new_campus_name
                new_campus_object.provider = provider
                new_campus_object.save()
                context['campus_error'] = ''
            else:
                context['campus_error'] = (
                    'Sorry, that campus name is already taken')
        # make sure logo has been uploaded before set the context
        # otherwise, let it empty
        if provider.provider_logo:
            context['provider_logo'] = provider.provider_logo.url

        return render(request, 'provider.html', context)
