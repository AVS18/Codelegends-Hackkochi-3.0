from django.db import models
from base.models import User
# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    faculty = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

class Enrollment(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE,related_name='student')
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    faculty = models.ForeignKey(User,on_delete=models.CASCADE,related_name='faculty')
    attendance = models.CharField(max_length=10,blank=True)
    grade = models.CharField(max_length=10,blank=True)

class ServiceRequest(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    message=models.CharField(max_length=2048)
    status=models.CharField(max_length=10,choices=(("Accepted","Accepted"),("Rejected","Rejected"),("Pending","Pending")),default="Pending")
    date = models.DateField(auto_now_add=True)