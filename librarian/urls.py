from django.urls import path
from . import views
urlpatterns = [
    path('dashboard',views.dashboard,name="dashboard"),
    path('addBook',views.addBook,name="addBook"),
    path('bookrequest',views.bookrequest,name="bookrequest"),
    path('acceptBookRequest/<str:bid>',views.acceptBookRequest,name="acceptBookRequest"),
    path('rejectBookRequest/<str:bid>',views.rejectBookRequest,name="rejectBookRequest"),
    path('alertUser',views.alertUser,name="alertUser"),
    path('makeAnnouncement',views.makeAnnouncement,name="makeAnnouncement")
]
