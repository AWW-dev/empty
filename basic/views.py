from django.shortcuts import render

# Create your views here.
from django.views import View


def home(request):
    return render(request, 'base.html')

def UserPanel(request):
    return render(request, 'userpanel.html')
