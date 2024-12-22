from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('course',views.course),
    path('view_course/<id>',views.view_course),
    path('placement',views.placement),
    
]