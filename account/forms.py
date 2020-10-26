import form as form
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import User
from django import forms

from django.contrib.auth.models import User

from account.models import UserProfile


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input-material'}),
            'email': forms.TextInput(attrs={'class': 'form-input-material'}),
            'password1': forms.TextInput(attrs={'class': 'form-input-material'}),
            'password2': forms.TextInput(attrs={'class': 'form-input-material'}),
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user', 'app']

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'password']