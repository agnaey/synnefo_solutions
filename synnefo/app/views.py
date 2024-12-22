from django.shortcuts import render
from .models import Courses,Review,Placement


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

def view_course(req,id):
    course=Courses.objects.get(id=id)
    placement=Placement.objects.all()[:4]
    placement1=Placement.objects.all()[4:8]
    return render(req,'view_course.html',{'course':course,'placement':placement,'placement1':placement1})

def placement(req):
    placement=Placement.objects.all()
    return render(req,'placement.html',{'placement':placement})