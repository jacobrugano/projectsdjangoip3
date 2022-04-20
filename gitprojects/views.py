from django.shortcuts import render,redirect
from .models import Category, Project
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views import generic

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


class AddLike(LoginRequiredMixin, View):
    def project(self, request, pk, *args, **kwargs):
        project = Project.objects.get(pk=pk)

        is_dislike = False

        for dislike in project.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            project.dislikes.remove(request.user)

        is_like = False

        for like in project.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            project.likes.add(request.user)

        if is_like:
            project.likes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

class AddDislike(LoginRequiredMixin, View):
    def project(self, request, pk, *args, **kwargs):
        project = Project.objects.get(pk=pk)

        is_like = False

        for like in project.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            project.likes.remove(request.user)

        is_dislike = False

        for dislike in project.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            project.dislikes.add(request.user)

        if is_dislike:
            project.dislikes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

class UserEditView(generic.CreateView):
    form_class = UserChangeForm
    template_name = 'gitprojects/edit_profile.html'
    success_url = reverse_lazy('home')