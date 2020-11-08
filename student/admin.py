from django.contrib import admin
from .models import Enrollment,Course
# Register your models here.
class CourseRef(admin.ModelAdmin):
    list_display = ['name','description','faculty']

admin.site.register(Course,CourseRef)

class EnrollRef(admin.ModelAdmin):
    list_display = ['student','course','faculty']
    list_filter = ['student','course','faculty']

admin.site.register(Enrollment,EnrollRef)