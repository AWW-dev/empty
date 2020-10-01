from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django import forms


from account.models import UserProfile
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
          model = User
          fields = ['username', 'email', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']