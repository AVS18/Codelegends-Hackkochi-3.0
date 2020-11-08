from django.urls import path
from . import views
urlpatterns = [
    path('dashboard',views.dashboard,name="dashboard"),
    path('enrollments',views.enrollments,name="enrollments"),
    path('studAnnouncement',views.studAnnouncement,name="studAnnouncement"),
    path('makeBookRequest',views.makeBookRequest,name="makeBookRequest"),
    path('requestService',views.requestService,name="requestService")
]
