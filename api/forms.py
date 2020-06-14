from django.contrib.auth.models import User
from django import forms
from django.core.validators import validate_email
from rest_framework.authtoken.models import Token


class UserRegistrationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(), required=True)
    name = forms.CharField(max_length=100, required=True)
    # phone = forms.IntegerField()

    def is_valid(self):
        valid = super(UserRegistrationForm, self).is_valid()
        if not valid:
            return False
        data = self.cleaned_data
        password = data['password']
        password2 = data['password2']
        name = data['name']
        email = data['email']
        # phone = data['phone']
        if self.request.user.is_authenticated:
            pass
        else:
            if name == "":
                valid = False
                self._errors['name'] = [u'Name should not be empty']
            elif len(name) > 30:
                valid = False
                self._errors['name'] = [u'Should be less than 30 characters']
        if self.request.user.is_authenticated:
            pass
        else:
            try:
                validate_email(email)
                valid = True
            except:
                valid = False
                self._errors['email'] = [u'Enter valid email']
        if password != password2:
            valid = False
            self._errors['password'] = [u'Passwords do not match']
        try:
            User.objects.get(username=data['email'])
            valid = False
            self._errors['email'] = [u'This Email id is already in use']
        except User.DoesNotExist:
            pass
        if len(password) < 6:
            valid = False
            self._errors['password'] = [u'Password should be at least 8 characters long']
        return valid

    def save(self, commit=True):
        data = self.cleaned_data
        if self.request.user.is_authenticated:
            user = User.objects.get(id=self.request.user.id)
            if data['name']:
                user.first_name = data['name']
            user.username = user.email
            user.set_password(data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return token
        else:
            user = User.objects.create(username=data['email'], email=data['email'], first_name=data['name'])
            user.set_password(data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return token