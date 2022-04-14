"""projectsdjangoip3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gitprojects.urls')),
    #  url(r'^accounts/', include('registration.backends.simple.urls')),
    path('authentication/', include('django.contrib.auth.urls')),
    path('authentication/', include('authentication.urls')),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
                # To add the static file as a url to the project urls 
                # This code says, go to settings then Pick MEDIA_URL
                # Then inside get a document in settings with MEDIA_ROOT
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
                # To register files such as css and js files
