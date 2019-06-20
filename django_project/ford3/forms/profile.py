from django import forms


class ProfileForm(forms.Form):
    first_name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(
            attrs={'placeholder': 'John'}
        ),
        required=True,
        max_length=100
    )
    last_name = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(
            attrs={'placeholder': 'Doe'}
        ),
        required=True,
        max_length=100
    )
    email = forms.EmailField(
        label='E-mail address',
        widget=forms.EmailInput(attrs={'placeholder': 'email@example.com'}),
        required=True
    )
