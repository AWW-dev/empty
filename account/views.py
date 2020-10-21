from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
# Create your views here.
from django.urls import reverse_lazy
from django.views import View, generic

from account.forms import RegisterForm, UserProfileForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect("/")
        else:
            print(form.errors)
    else:
        form = RegisterForm()
        profile_form = UserProfileForm()
    return render(request, 'registration/registration.html', {"form": form, 'profile_form': profile_form})


def ShowProfileView(request, id):
    user = User.objects.get(id=id)
    return render(request, 'profil.html', {'user': user})

class UserEditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

