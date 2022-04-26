from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})

def settingsPage(request):
    tenant = get_tenant(request)
    imagePath = tenant.image.url
    context = {'tenant': tenant, 'imagePath': imagePath}
    return render(request, 'setting/settings.html', context)
