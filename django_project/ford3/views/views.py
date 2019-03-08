from django.shortcuts import render # noqa

# Create your views here.
from django.shortcuts import render_to_response


def provider_form(request):
    return render_to_response('provider_form.html')

def test_widgets(request):
    return render_to_response('test_widgets.html')


