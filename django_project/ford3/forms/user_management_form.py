from django import forms
from django.core.validators import validate_email
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _


class UserManagementForm(forms.Form):
    group = forms.CharField(
        widget=forms.HiddenInput,
        required=True)
    email_confirmed = forms.BooleanField(
        widget=forms.CheckboxInput,
        required=False)
    email = forms.EmailField(
        widget=forms.EmailInput,
        required=True)
    error_messages = {
        'invalid_email': _("Invalid email"),
    }

    def clean_email(self):
        email = self.cleaned_data['email']
        validate_email(email)
        return email


class UserManagementPasswordResetForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput,
        required=False,
        max_length=50
    )
    last_name = forms.CharField(
        widget=forms.TextInput,
        required=False,
        max_length=50
    )
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput,
    )
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', '')
        super().__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        password_validation.validate_password(password2, self.user)
        return password2

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user
