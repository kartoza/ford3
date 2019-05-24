from ford3.models.user_management import UserManagement
from ford3.forms.user_management_form import UserManagementForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User, Group
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.urls import reverse
from django.http import Http404


def show(request):
    group_id = request.user.groups.all().first().id
    if group_id == 1:
        user_mgmt = UserManagement.provider_objects.all()
    elif group_id == 3:
        user_mgmt = UserManagement.campus_objects.all()
    elif group_id == 2:
        return Http404("You can't be here")
    # superuser
    else:
        user_mgmt = UserManagement.objects.all()
    context = {
        'user_management': user_mgmt,
    }
    return render(request, "user_mgmt/show.html", context)


def add(request):
    if request.method == "POST":
        email = request.POST['email']
        group_name = request.POST['group']
        user = User.objects.create_user(username=email, email=email)
        group = Group.objects.get(name=group_name)
        user.groups.add(group)
        user.save()
        user.is_active = False

        um = UserManagement(user=user, group=group, email_confirmed=False)
        um.save()

        current_site = get_current_site(request)
        subject = 'Activate your account'
        message = render_to_string(
            'registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(
                    force_bytes(user.pk)).decode(),
                'token': default_token_generator.make_token(user),
                # 'token': account_activation_token.make_token(user),
            })
        user.email_user(subject, message)
        return redirect("show-usermgmt")
    else:
        group_name = request.user.groups.all().first().name
        allowed_group = ''
        if group_name == 'Provinces':
            allowed_group = 'Providers'
        elif group_name == 'Providers':
            allowed_group = 'Campus'

        data = {'group': allowed_group}
        form = UserManagementForm(initial=data)
        return render(request, "user_mgmt/add.html", {'form': form})


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
    form = UserManagementForm(request.POST)
    # update to db, ignore updating group
    user.email = request.POST['email']
    user_mgmt.email_confirmed = bool(form.fields['email_confirmed'])

    user.save()
    user_mgmt.save()
    return redirect("show-usermgmt")


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
        user = User.objects.get(pk=uid)
        user_mgmt = get_object_or_404(UserManagement, user_id=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user_mgmt.email_confirmed = True
        # user.profile.email_confirmed = True
        user.save()
        user_mgmt.save()
        password_reset = reverse(
            'password_reset_confirm',
            kwargs={'uidb64': uidb64, 'token': token})
        return redirect(password_reset)
    else:
        return render(request, 'registration/account_activation_invalid.html')
