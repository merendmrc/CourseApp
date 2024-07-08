from django.contrib import admin
from .models import Course,Category

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title","is_active","date","category_list")
    list_filter = ("is_active",)
    list_editable = ("is_active",)
    search_fields = ("title","description")
    prepopulated_fields = {"slug": ("title",)}
    
    def category_list(self,obj):
        html= ""
        for category in obj.categories.all():
            html+= category.name + " "
        return html

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","slug","course_count")
    prepopulated_fields = {"slug": ("name",)}

    def course_count(self,obj):
        return obj.courses.count()


