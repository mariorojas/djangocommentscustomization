from django.shortcuts import render

from .models import Profile


def index(request):
    profile = Profile.objects.get(pk=1)
    return render(request, 'index.html', {'profile': profile})
