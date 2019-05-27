from ford3.models.user_management import UserManagement
from ford3.forms.user_management_form import (
    UserManagementForm,
    UserManagementPasswordResetForm
)
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User, Group
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.urls import reverse
import datetime
from pytz import UTC
from base.views.error_views import custom_403, custom_404
from django.conf import settings

VALID_LINK_DAYS = getattr(settings, 'VALID_LINK_DAYS', 1)


def show(request):
    # prepare to list user management
    # for admin
    if request.user.is_staff:
        user_mgmt = UserManagement.objects.all()
        # admin can add a user belongs to Provinces
        allowed_group = 'Provinces'
    else:
        # for non-admins
        group_id = request.user.groups.all().first().id
        if group_id == 1:
            user_mgmt = UserManagement.provider_objects.all()
        elif group_id == 3:
            user_mgmt = UserManagement.campus_objects.all()
        elif group_id == 2:
            return custom_403(request)
        # prepare form for add new user
        group_name = request.user.groups.all().first().name
        allowed_group = ''
        if group_name == 'Provinces':
            allowed_group = 'Providers'
        elif group_name == 'Providers':
            allowed_group = 'Campus'

    data = {'group': allowed_group}
    form = UserManagementForm(initial=data)

    context = {
        'user_management': user_mgmt,
        'form': form
    }
    return render(request, "user_mgmt/show.html", context)


def add(request):
    form = UserManagementForm(data=request.POST)
    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data['email']
            group_name = form.cleaned_data['group']
            user = User.objects.create_user(username=email, email=email)
            group = Group.objects.get(name=group_name)
            user.groups.add(group)
            user.is_active = False
            user.save()
            user.is_active = False

            um = UserManagement(user=user, group=group, email_confirmed=False)
            um.save()

            current_site = get_current_site(request)
            subject = 'Activate your account'
            message = render_to_string(
                'user_mgmt/account_activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(
                        force_bytes(user.pk)).decode(),
                    'token': default_token_generator.make_token(user),
                })
            user.email_user(subject, message)
            return redirect("show-usermgmt")
        else:
            # prepare to list user management
            group_id = request.user.groups.all().first().id
            if group_id == 1:
                user_mgmt = UserManagement.provider_objects.all()
            elif group_id == 3:
                user_mgmt = UserManagement.campus_objects.all()
            elif group_id == 2:
                return custom_403(request)
            # superuser
            else:
                user_mgmt = UserManagement.objects.all()
            context = {
                'user_management': user_mgmt,
                'form': form
            }
            return render(request, "user_mgmt/show.html", context)
    else:
        return custom_404(request)


def edit(request, user_id):
    user_mgmt = get_object_or_404(UserManagement, user_id=user_id)
    data = {
        'email': user_mgmt.user.email,
        'group': user_mgmt.group.name,
        'email_confirmed': user_mgmt.email_confirmed
    }
    form = UserManagementForm(data)

    context = {
        'form': form,
        'user_id': user_id
    }
    return render(request, "user_mgmt/edit.html", context)


def update(request, user_id):
    user_mgmt = get_object_or_404(UserManagement, user_id=user_id)
    user = get_object_or_404(User, id=user_id)
    form = UserManagementForm(data=request.POST)
    if form.is_valid():
        # update to db, ignore updating group
        user.email = form.cleaned_data['email']
        user_mgmt.email_confirmed = form.cleaned_data['email_confirmed']

        user.save()
        user_mgmt.save()
        return redirect("show-usermgmt")
    else:
        context = {
            'form': form,
            'user_id': user_id
        }
        return render(request, "user_mgmt/edit.html", context)


def enable(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_active = True

    user.save()
    return redirect("show-usermgmt")


def disable(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_active = False

    user.save()
    return redirect("show-usermgmt")


def destroy(request, user_id):
    user_mgmt = UserManagement.objects.get(user_id=user_id)
    user = get_object_or_404(User, id=user_id)
    user.delete()
    user_mgmt.delete()
    return redirect("show-usermgmt")


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = get_object_or_404(User, pk=uid)
        user_mgmt = get_object_or_404(UserManagement, user_id=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user_mgmt.email_confirmed = True
        # check if the link still valid
        valid_date = user.date_joined + datetime.timedelta(
            days=VALID_LINK_DAYS)
        current_date = datetime.datetime.now()
        valid_date = valid_date.replace(tzinfo=UTC)
        current_date = current_date.replace(tzinfo=UTC)

        if current_date > valid_date:
            return render(request, 'user_mgmt/account_activation_invalid.html')
        user.save()
        user_mgmt.save()
        # go to account activation first, no to reset password
        password_reset = reverse(
            'active_then_set_password',
            kwargs={
                'uidb64': uidb64,
                'token': token
            })
        return redirect(password_reset)
    else:
        return render(request, 'user_mgmt/account_activation_invalid.html')


def password_reset(request, uidb64, token):
    uid = force_text(urlsafe_base64_decode(uidb64))
    user = get_object_or_404(User, pk=uid)
    if user is None or not default_token_generator.check_token(user, token):
        return render(request, 'user_mgmt/account_activation_invalid.html')

    if request.method == "POST":
        form = UserManagementPasswordResetForm(data=request.POST, user=user)
        if form.is_valid():
            # update user's detail
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.save()
            form.save()
            return redirect("active_then_set_password_done")
        else:
            return render(
                request,
                "user_mgmt/password_reset_confirm.html",
                {'form': form})
    else:
        form = UserManagementPasswordResetForm()
        return render(
            request,
            "user_mgmt/password_reset_confirm.html",
            {'form': form})


def password_reset__done(request):
    return render(request, "user_mgmt/password_reset_confirm_done.html")
