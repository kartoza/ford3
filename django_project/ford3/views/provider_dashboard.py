from django.shortcuts import (
    render
)
from ford3.models.provider import Provider


# @login_required
def show(request):
    providers = Provider.objects.all()
    # provider = get_object_or_404(
    #     Provider,
    #     id=provider_id)
    context = {
        'providers': list(providers)
    }
    return render(request, 'provider_dashboard.html', context)
