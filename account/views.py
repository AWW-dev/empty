from django.shortcuts import render, redirect


# Create your views here.
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
        form = RegisterForm()
        profile_form = UserProfileForm()
    return render(request, 'registration.html', {"form": form, 'profile_form': profile_form})