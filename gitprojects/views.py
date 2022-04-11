from django.shortcuts import render
from .models import Category, Project

# Create your views here.
def gallery(request):
    categories = Category.objects.all()
    return render(request, 'gitprojects/gallery.html', {"categories":categories})


def viewProject(request, pk):
    return render(request, 'gitprojects/project.html')


def addProject(request):
    return render(request, 'gitprojects/add.html')
