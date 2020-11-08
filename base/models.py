from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    user_type = models.CharField(max_length=10,choices=(('Student','Student'),('Faculty','Faculty'),('Librarian','Librarian')),null=True)

class SiteAnnouncement(models.Model):
    message = models.CharField(max_length=500)
    link_exist = models.BooleanField()
    link = models.CharField(max_length=500,null=True,blank=True)
    date = models.DateField(auto_now_add=True,null=True)

class StudentAnnouncement(models.Model):
    announce_from = models.ForeignKey(User,on_delete=models.CASCADE)
    message= models.CharField(max_length=2048)
    date = models.DateField(auto_now_add=True)