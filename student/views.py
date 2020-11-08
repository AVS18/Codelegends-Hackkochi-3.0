from django.shortcuts import render,redirect
from django.contrib import messages,auth
from .models import Enrollment,ServiceRequest
from base.models import StudentAnnouncement
from librarian.models import Book, BookRequest
def check(request):
    return request.user.user_type=="Student"

# Create your views here.
def dashboard(request):
    if not check(request):
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Invalid Request')
        return redirect('/')
    
    if request.user.is_authenticated:
        return render(request,'studentDashboard.html')
    else:
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Not Logged In')
        return redirect('/')
    
def enrollments(request):
    if not check(request):
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Invalid Request')
        return redirect('/')
    
    if not request.user.is_authenticated:
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Not Logged In')
        return redirect('/')
    courses = Enrollment.objects.filter(student=request.user)
    return render(request,'studentCourses.html',{'courses':courses})

def studAnnouncement(request):
    if not check(request):
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Invalid Request')
        return redirect('/')
    
    if not request.user.is_authenticated:
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Not Logged In')
        return redirect('/')
    announcements=StudentAnnouncement.objects.all()
    return render(request,'studAnnBoard.html',{'announcements':announcements})

def makeBookRequest(request):
    if not check(request):
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Invalid Request')
        return redirect('/')
    
    if not request.user.is_authenticated:
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Not Logged In')
        return redirect('/')   
    if request.method=="POST":
        book = request.POST["book"]
        return_date = request.POST["return_date"]
        BookRequest.objects.create(requested_by=request.user,return_date=return_date,book=Book.objects.get(name=book))
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,f'{book} Book Request Placed Successfully')
        return redirect('/student/dashboard')
    old_request=BookRequest.objects.filter(requested_by=request.user)
    books = Book.objects.all()
    return render(request,'makeBookRequest.html',{'old':old_request,'books':books})


def requestService(request):
    if not check(request):
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Invalid Request')
        return redirect('/')
    
    if not request.user.is_authenticated:
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Not Logged In')
        return redirect('/')
    if request.method=="POST":
        name=request.POST["name"]
        message=request.POST["message"]
        ServiceRequest.objects.create(name=name,user=request.user,message=message)
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Request Placed Successfully')
        return redirect('/student/dashboard')
    my_request=ServiceRequest.objects.filter(user=request.user)
    return render(request,'requestService.html',{'my_request':my_request})