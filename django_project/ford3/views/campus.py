from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_http_methods

from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)
from django.db import DataError
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.datastructures import MultiValueDictKeyError
from ford3.models.campus import Campus
from ford3.models.provider import Provider
from ford3.decorators import provider_check, campus_check


@login_required
@provider_check
@campus_check
def show(request, provider_id, campus_id):
    campus = get_object_or_404(
        Campus,
        id=campus_id)
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


@login_required
@permission_required('ford3.add_campus', raise_exception=True)
@provider_check
def create(request, provider_id):
    if request.method == 'GET':
        url = reverse('show-provider', args=[str(provider_id)])
        return redirect(url)


    provider = get_object_or_404(
        Provider,
        id=provider_id)

    context = {
        'provider': provider
    }

    try:
        provider.campus_set.create(
            name=request.POST['campus_name'],
            created_by=request.user,
            edited_by=request.user)
        context['campus_success'] = 'Campus successfully created.'
    except ValidationError as ve:
        context['campus_error'] = '<br />'.join(ve.messages)
    except MultiValueDictKeyError:
        # arg campus_name not present in request.POST
        context['campus_error'] = 'Bad request.'
    except DataError:
        context['campus_error'] = 'Campus name is too long. (255 characters maximum)' # noqa
    return render(request, 'provider.html', context)


@login_required()
@permission_required('ford3.delete_provider', raise_exception=True)
@require_http_methods(['GET'])
@provider_check
@campus_check
def delete(request, provider_id, campus_id):
    campus = get_object_or_404(
        Campus,
        id=campus_id
    )

    campus.deleted = True
    campus.deleted_by = request.user
    campus.save()

    return redirect(reverse('dashboard'))
