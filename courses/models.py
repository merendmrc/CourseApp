from django.db import models
          
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(default="", unique=True, blank=True, editable=False ,db_index=True)

    def __str__(self) -> str:
        return self.name
    
class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(default="", unique=True, blank=False, db_index=True)
    categories = models.ManyToManyField(Category,related_name="courses")
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
