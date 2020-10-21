from django.contrib.auth.models import User
from django.db import models

from apps.models import App


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=250, verbose_name="Jak firmę reprezentujesz?")
    app = models.ManyToManyField(App)