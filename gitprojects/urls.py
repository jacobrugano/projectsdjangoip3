from django.urls import path
# from django.conf.urls import url
from . import views 
from .views import AddLike, AddDislike

urlpatterns = [
    path('', views.gallery, name='gallery'), # Our homepage
    path('project/<str:pk>/', views.viewProject, name='project'), # photo/<str:pk>/ to get photo by id or primary key
    path('add/', views.addProject, name='add'),
    path('search/', views.search_results, name='search_results'),
    path('post/<int:pk>/like', AddLike.as_view(), name='like'),
    path('post/<int:pk>/dislike', AddDislike.as_view(), name='dislike'),
]
