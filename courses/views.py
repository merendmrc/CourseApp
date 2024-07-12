from datetime import date
from django.shortcuts import get_object_or_404, render,redirect
from .models import Course,Category
from django.core.paginator import Paginator

def index(req):
    courses = Course.objects.all()
    categories = Category.objects.all()

    paginator = Paginator(courses, 2)
    page = req.GET.get('page',1)
    page_obj = paginator.page(page)

    return render(req, template_name="courses/index.html", context={
        'categories': categories,
        'page_obj': page_obj
    })

def details(req, slug):
    course = get_object_or_404(Course, slug=slug)
    context ={
        'course': course
    }
    return render(req, template_name="courses/details.html", context=context)


def getCoursesByCategoryName(req, slug):
    kurslar = Course.objects.filter(categories__slug=slug).order_by("is_active")
    kategoriler = Category.objects.all()

    paginator = Paginator(kurslar, 2)
    page = req.GET.get('page',1)
    page_obj = paginator.page(page)

    return render(req, template_name="courses/index.html", context={
        "page_obj" : page_obj,
        "categories" : kategoriler,
        "selected_category_id" : Category.objects.get(slug=slug).id
    })