from django.db import models

# Create your models here.
from django.contrib.auth.models import User
# Create your models here.

class Courses(models.Model):
    name=models.TextField()
    img=models.FileField()
    description=models.TextField()
    
class Contact(models.Model):
    name = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    
class Placement(models.Model):
    name=models.TextField()
    course_name=models.TextField()
    img=models.FileField()
    company=models.TextField()