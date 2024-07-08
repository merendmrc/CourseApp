from datetime import date
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse,HttpResponseNotFound,Http404
from django.urls import reverse
from .models import Course,Category

def index(req):
    courses = Course.objects.all()
    categories = Category.objects.all()

    return render(req, template_name="courses/index.html", context={
        'categories': categories,
        'courses':courses
    })

def details(req, slug):
    course = get_object_or_404(Course, slug=slug)
    context ={
        'course': course
    }
    return render(req, template_name="courses/details.html", context=context)


def getCoursesByCategoryName(req, slug):
    kurslar = Course.objects.filter(categories__slug=slug)
    kategoriler = Category.objects.all()
    return render(req, template_name="courses/index.html", context={
        "courses" : kurslar,
        "categories" : kategoriler,
        "selected_category_id" : Category.objects.get(slug=slug).id
    })