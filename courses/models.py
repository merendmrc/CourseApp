from django.db import models
from ckeditor.fields import RichTextField
          
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(default="", unique=True, blank=True, editable=False ,db_index=True)

    def __str__(self) -> str:
        return self.name
    
class Course(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100, default="")
    description = RichTextField()
    image = models.ImageField(upload_to="images", default="")
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(default="", unique=True, blank=False, db_index=True)
    categories = models.ManyToManyField(Category,related_name="courses")
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
    
class Slider(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images")
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.title}"

class UploadImage(models.Model):
    image = models.ImageField(upload_to="images")