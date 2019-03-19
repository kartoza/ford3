from django import forms
from ford3.models.provider import Provider


EMPTY_TEL_ERROR = 'Please enter your telephone number'


class ProviderForm(forms.models.ModelForm):

    class Meta:
        model = Provider
        fields = ('telephone',)
        widgets = {
            'telephone': forms.fields.TextInput(
                attrs={'placeholder': '••• ••• ••••'})
        }
        error_messages = {
            'telephone': {'required': EMPTY_TEL_ERROR}
        }
