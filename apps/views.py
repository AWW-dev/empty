from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View

from apps.models import App


def ShowAppsView(request, id):
    apps = App.objects.all()

    name = User.objects.get(id=id)
    name_apps = App.objects.filter(userprofile=name.userprofile)
    return render(request, 'apps.html', {'apps': apps, 'name': name, 'name_apps': name_apps})
