from django.shortcuts import render

# Create your views here.
def gallery(request):
    return render(request, 'gitprojects/gallery.html')


def viewProject(request, pk):
    return render(request, 'gitprojects/project.html')


def addProject(request):
    return render(request, 'gitprojects/add.html')
