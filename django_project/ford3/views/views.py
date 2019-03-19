from django.shortcuts import render # noqa
from django.shortcuts import render_to_response

# Create your views here.
from ford3.models.provider import Provider



def provider_form(request):
    if request.method == 'POST':
        new_provider = Provider()
        provider_tel = request.POST['provider_tel']
        new_provider.telephone = provider_tel
        new_provider.save()
    else:
        provider_tel = ''
    return render(request, 'provider_form.html', {
        'provider_tel': provider_tel})

        # provider_test_object_instance = Provider(
        #     id=2,
        #     name='Object Test Name',
        #     website='www.mytest.com',
        #     logo_url='http://sometestplaceholder/logo.png',
        #     email='Test@test.com',
        #     admissions_contact_no='0137527576',
        #     postal_address='1200',
        #     physical_address='Some long physical address',
        #     telephone='27821233322',
        #     provider_type='Technicon',
        # )


        # return render(request, 'provider_form.html')
        # if a GET (or any other method) we'll create a blank form

    # else:
    #     return render(request, 'provider_form.html')


def test_widgets(request):
    return render_to_response('test_widgets.html')
