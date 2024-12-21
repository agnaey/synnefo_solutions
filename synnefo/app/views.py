from django.shortcuts import render
from .models import Courses,Review


# Create your views here.

def index(request):
    course=Courses.objects.all()[:4]
    course1=Courses.objects.all()[4:8]
    reviews=Review.objects.all()[:3]
    reviews1=Review.objects.all()[3:6]
    return render(request,'index.html',{'course':course,'course1':course1,'reviews':reviews,'reviews1':reviews1})

def course(req):
    course=Courses.objects.all()
    return render(req,'course.html',{'course':course})