from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from ford3.models.provider import Provider
from ford3.models.province import Province
from ford3.models.provider_users_campus_users import ProviderUsersCampusUsers
from django.contrib.auth.models import User, Group, Permission


@login_required
def show(request):
    user = request.user
    user_id = user.id
    permission = Permission.objects.filter(name='Is Province User').first()
    if user.has_perm('ford3.province_user'):
        user_group = 'province'
    elif user.has_perm('ford3.provider_user'):
        user_group = 'provider'
    elif user.has_perm('ford3.campus_user'):
        user_group = 'campus'
    else:
        user_group = 0
    if not user_group:
        return redirect(reverse('home'))
    if user_group == 'province':
        user_province: Province = (
            Province.objects.filter(users__id=user_id).first())
        providers = Provider.objects.filter(province_id=user_province.id)
    if user_group == 'provider':  # Provider user
        providers = Provider.objects.filter(users__id=user_id)
    if user_group == 'campus':  # Campus user
        provider_user = ProviderUsersCampusUsers.objects.filter(
            campus_user_id=user_id).first()
        provider_user = provider_user.provider_user_id
        providers = Provider.objects.filter(users__id=provider_user.id)

    context = {
        'providers': list(providers)
    }
    return render(request, 'provider_dashboard.html', context)
