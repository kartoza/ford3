from django.shortcuts import render, redirect, render_to_response
from django.db import transaction
from ford3.models.provider import Provider
from ford3.forms.provider_form import ProviderForm


def provider_form(request):
    if request.method == 'POST':
        form = ProviderForm(request.POST)
        if form.is_valid():
            new_provider = Provider()
            provider_type = form.cleaned_data['provider_type']
            telephone = form.cleaned_data['telephone']
            email = form.cleaned_data['email']
            physical_address_line_1 = form.cleaned_data['physical_address_line_1']
            physical_address_line_2 = form.cleaned_data['physical_address_line_2']
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

            number_of_campuses = request.POST['number-of-campuses']

            new_provider.save()

            return redirect('/')

    else:
        form = ProviderForm()
    return render(request, 'provider_form.html', {'form': form})


def widget_examples(request):
    return render_to_response('test_widgets.html')
