from django.urls import path
from . import views
urlpatterns = [
    path('dashboard',views.dashboard,name="dashboard"),
    path('facCourses',views.facCourses,name="facCourses"),
    path('enrollment',views.enrollment,name="enrollment"),
    path('displayStudents',views.displayStudents,name="displayStudents"),
    path('updateGrade',views.updateGrade,name="updateGrade"),
    path('updateAttendance',views.updateAttendance,name="updateAttendance"),
    path('facAnnouncement',views.facAnnouncement,name="facAnnouncement")
]
