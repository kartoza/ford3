from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from ford3.models.provider import Provider
from ford3.models.province import Province
from ford3.models.provider_users_campus_users import ProviderUsersCampusUsers

@login_required
def show(request):

    user = request.user
    user_id = user.id
    user_groups = user.groups.all()
    for next_group in user_groups:
        if next_group.id == 3:
            user_group_id = 3
        elif next_group.id == 2:
            user_group_id = 2
        elif next_group.id == 1:
            user_group_id = 1
    if user_group_id == 1:  # Province user sees all providers in his province
        user_province: Province = (
            Province.objects.filter(users__id=user_id).first())
        providers = Provider.objects.filter(province_id=user_province.id)
    if user_group_id == 3:  # Provider user
        providers = Provider.objects.filter(users__id=user_id)
    if user_group_id == 2:  # Campus user
        provider_user = ProviderUsersCampusUsers.objects.filter(
            campus_user_id=user_id).first()
        providers = Provider.objects.filter(users__id=provider_user.id)

    context = {
        'providers': list(providers)
    }
    return render(request, 'provider_dashboard.html', context)
