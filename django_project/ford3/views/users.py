from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse


@login_required()
def create_provider_user(request):
    current_user: User = request.user
    if 'Provinces' not in current_user.groups:
        redirect(reverse('Login'))
    username = request.POST['provider_username']
    password = request.POST['provider_password']
    email = request.POST['provider_email']
    provider_user = get_user_model().objects.create_user(
        username,
        password,
        email)
    providers_group: Group = Group.objects.get(pk=3)
    provider_user.groups.add(providers_group)

