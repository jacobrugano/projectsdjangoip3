from django.shortcuts import render
from .models import Category, Project

# Create your views here.
def gallery(request):
    categories = Category.objects.all()
    projects = Project.objects.all()
    return render(request, 'gitprojects/gallery.html', {"categories":categories, "projects":projects})


def viewProject(request, pk):
    return render(request, 'gitprojects/project.html')


def addProject(request):
    return render(request, 'gitprojects/add.html')
