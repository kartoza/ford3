from django import forms
from ford3.models.provider import Provider


EMPTY_TEL_ERROR = 'Your telephone number is required.'
EMPTY_EMAIL_ERROR = 'Your email is required.'


class ProviderForm(forms.models.ModelForm):

    class Meta:
        model = Provider
        fields = ('telephone', 'email')
        widgets = {
            'telephone': forms.fields.TextInput(
                attrs={'placeholder': '••• ••• ••••'}),
            'email':  forms.fields.EmailInput()
        }
        error_messages = {
            'telephone': {'required': EMPTY_TEL_ERROR},
            'email' : {'required': EMPTY_EMAIL_ERROR}
        }
