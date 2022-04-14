from unicodedata import category
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.name


# class Photo
class Project(models.Model):

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
                                       # blank=True so that it is not a requirement to select category when adding a project
                                       # on_delete=models.SET_NULL AND null=True, go together
    image = models.ImageField(null=False, blank=False)
    # description = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField()
    likes = models.ManyToManyField(Category, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(Category, blank=True, related_name='dislikes')


    @classmethod
    def search_by_title(cls,search_term):
        category = cls.objects.filter(title__icontains=search_term)
        return category

    def __str__(self):
        return self.description
