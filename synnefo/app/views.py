from django.shortcuts import render
from .models import Courses


# Create your views here.

def index(request):
    course=Courses.objects.all()[:4]
    course1=Courses.objects.all()[4:8]
    return render(request,'index.html',{'course':course,'course1':course1})
