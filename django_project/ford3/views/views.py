from django.shortcuts import render, redirect, render_to_response
from ford3.models.provider import Provider
from ford3.forms.provider_form import ProviderForm


def provider_form(request):
    if request.method == 'POST':
        form = ProviderForm(request.POST)
        if form.is_valid():
            new_provider = Provider()
            telephone = form.cleaned_data['telephone']
            new_provider.telephone = telephone
            new_provider.save()
            return redirect('/')
    else:
        form = ProviderForm()
    return render(request, 'provider_form.html', {'form': form})


def widget_examples(request):
    return render_to_response('test_widgets.html')
