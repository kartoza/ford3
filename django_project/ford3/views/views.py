from django.shortcuts import (
    render,
    get_object_or_404,
    render_to_response
)
from ford3.models import (
    Campus,
    Qualification
)
from base.views import custom_404


def show_campus(request, provider_id, campus_id):
    campus = get_object_or_404(
        Campus,
        id=campus_id)

    # prevent a knowledgeable user looks at deleted provider
    if campus.provider.deleted:
        return custom_404(request)

    form_data = {
        'provider_name': campus.provider.name
    }
    context = {
        'form_data': form_data,
        'campus': campus,
        'provider': campus.provider,
        # make sure logo has been uploaded before set the context
        # otherwise, let it empty
        'provider_logo':
            campus.provider.provider_logo.url
            if campus.provider.provider_logo else ""
    }

    return render(request, 'campus.html', context)


def show_qualification(request, provider_id, campus_id, qualification_id):
    qualification = get_object_or_404(
        Qualification,
        id=qualification_id)

    # prevent a knowledgeable user looks at deleted provider
    if qualification.campus.provider.deleted:
        return custom_404(request)

    context = {
        'qualification': qualification,
        'provider': qualification.campus.provider,
        # make sure logo has been uploaded before set the context
        # otherwise, let it empty
        'provider_logo':
            qualification.campus.provider.provider_logo.url
            if qualification.campus.provider.provider_logo else ""
    }
    return render(request, 'qualification.html', context)


def widget_examples(request):
    return render_to_response('test_widgets.html')
