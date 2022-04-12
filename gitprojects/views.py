from django.shortcuts import render,redirect
from .models import Category, Project

# Create your views here.
def gallery(request):
    categories = Category.objects.all()
    projects = Project.objects.all()
    return render(request, 'gitprojects/gallery.html', {"categories":categories, "projects":projects})


def viewProject(request, pk):
    project = Project.objects.get(id=pk)
    return render(request, 'gitprojects/project.html', {'project':project})


def addProject(request):
    categories = Category.objects.all()

    # To capture the data uploaded by the form:
    # First verify that there is actual data submitted thro:
    if request.method == 'POST': #To check the request type is POST
        data = request.POST #To get the form-fields data
        project = request.FILES.get('project') #To get the uploaded project, project  been the name of that upload button in html
   
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category = None
        
        photo = Photo.objects.create(
            category=category,
            description=data['description'],
            image=image,
        )

        return redirect('gallery')


    return render(request, 'gitprojects/add.html', {'categories':categories})
