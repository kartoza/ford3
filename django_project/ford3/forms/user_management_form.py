from django import forms
from django.contrib.auth.models import User


class UserManagementForm(forms.Form):
    user_name = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.TextInput,
        required=True)
    group = forms.CharField(
        widget=forms.TextInput,
        required=True)
    email_confirmed = forms.BooleanField(
        widget=forms.CheckboxInput,
        required=False)
    email = forms.EmailField(
        widget=forms.EmailInput,
        required=True)
