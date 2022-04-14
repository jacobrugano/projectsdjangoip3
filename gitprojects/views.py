from django.shortcuts import render,redirect
from .models import Category, Project

# Create your views here.
def gallery(request):
    category = request.GET.get('category')
    if category == None:
        projects = Project.objects.all()
    else:
        projects = Project.objects.filter(category__name=category)

    categories = Category.objects.all()
    context = {'categories': categories, 'projects': projects}
    return render(request, 'gitprojects/gallery.html', context)

    # # categories = Category.objects.all()
    # projects = Project.objects.all()
    # return render(request, 'gitprojects/gallery.html', {"categories":categories, "projects":projects})
    # category = request.GET.get('category')
    # if category == None:
    #     photos = Photo.objects.filter(category__user=user)
    # else:
    #     photos = Photo.objects.filter(
    #         category__name=category, category__user=user)

    # categories = Category.objects.all(user=user)
    # context = {'categories': categories, 'photos': photos}
    # return render(request, 'photos/gallery.html', context)



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
        
        project = Project.objects.create(
            category=category,
            description=data['description'],
        )

        return redirect('gallery')


    return render(request, 'gitprojects/add.html', {'categories':categories})


def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_articles = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'gallery.html',{"message":message,"category": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})
