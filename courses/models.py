from django.db import models
from django.utils.text import slugify

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50)
    date = models.DateField()
    is_active = models.BooleanField()
    slug = models.SlugField(default="", unique=True, db_index=True)

    def __str__(self) -> str:
        return self.title
    
    def save(self,*args,**kwargs):
        slug = slugify(self.title)
        super().save(args,kwargs)
        
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
