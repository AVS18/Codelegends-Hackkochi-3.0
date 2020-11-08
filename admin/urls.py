from django.urls import path
from . import views
urlpatterns = [
    path('dashboard',views.dashboard,name="dashboard"),
    path('addCourse',views.addCourse,name="addCourse"),
    path('site',views.site,name="site"),
    path('admEnrolledStudents',views.admEnrolledStudents,name="admEnrolledStudents"),
    path('requests',views.requests,name="requests"),
    path('acceptServiceRequest/<str:sid>',views.acceptServiceRequest,name="acceptServiceRequest"),
    path('rejectServiceRequest/<str:sid>',views.rejectServiceRequest,name="rejectServiceRequest")
]
