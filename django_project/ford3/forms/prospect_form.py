from django import forms
from ford3.models.prospect import Prospect


class ProspectForm(forms.models.ModelForm):
    class Meta:
        model = Prospect
        name = forms.CharField(label='Your name', required=True)
        fields = ['name', 'telephone', 'email']

        widgets = {
            'name': forms.fields.TextInput(
                attrs={'placeholder': 'Your name'}),
            'telephone': forms.fields.TextInput(
                attrs={'placeholder': 'Primary contact number'}),
            'email': forms.fields.EmailInput(
                attrs={'placeholder': 'example@example.com'}),
        }
