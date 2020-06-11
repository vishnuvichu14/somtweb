from django.contrib.auth.models import User
from django import forms


class UserRegistrationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(), required=True)
    name = forms.CharField(max_length=100, required=True)
    phone = forms.IntegerField()