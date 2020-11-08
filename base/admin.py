from django.contrib import admin
from .models import User,SiteAnnouncement,StudentAnnouncement
# Register your models here.

admin.site.register(User)
class SiteRef(admin.ModelAdmin):
    list_display=['date','message']

admin.site.register(SiteAnnouncement,SiteRef)

class StudentRef(admin.ModelAdmin):
    list_display=['announce_from','message','date']
    list_filter = ['announce_from','date']

admin.site.register(StudentAnnouncement,StudentRef)