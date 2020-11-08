from django.shortcuts import render,redirect
from django.contrib import messages
from base.models import User,SiteAnnouncement
from student.models import Course,Enrollment,ServiceRequest
# Create your views here.
def check(request):
    return request.user.is_superuser
        
def addCourse(request):
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
        name = request.POST['name']
        description = request.POST['description']
        faculty = request.POST["fac_name"]
        Course.objects.create(name=name,description=description,faculty=User.objects.get(first_name=faculty))
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Course Added Successfully')
        return redirect('/dadmin/dashboard')
    obj = User.objects.filter(user_type="Faculty")
    courses = Course.objects.all()
    return render(request,'addCourse.html',{'obj':obj,'courses':courses})

def dashboard(request):
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
    return render(request,'adminDashboard.html')

def site(request):
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
        message = request.POST["message"]
        link_exist = request.POST["link_exist"]
        link = request.POST["link"]
        SiteAnnouncement.objects.create(message=message,link_exist=link_exist,link=link)
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Information Announced Successfully')
        return redirect('/dadmin/dashboard')
    announcements=SiteAnnouncement.objects.all()
    return render(request,'siteAnnouncements.html',{'announcements':announcements})

def admEnrolledStudents(request):
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
    enrollment = Enrollment.objects.all()
    return render(request,'admEnrolledStudents.html',{'enrollment':enrollment})

def requests(request):
    if not check(request):
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Invalid Request')
        return redirect('/')
    pending_request = ServiceRequest.objects.filter(status="Pending")
    all_request = ServiceRequest.objects.all()
    return render(request,"showRequest.html",{'pending':pending_request,'all':all_request})

def acceptServiceRequest(request,sid):
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
    obj = ServiceRequest.objects.get(id=sid)
    obj.status="Accepted"
    obj.save(force_update=True)
    storage = messages.get_messages(request)
    storage.used = True
    messages.info(request,f'Service Request Accepted Successfully')
    return redirect('/dadmin/dashboard')

def rejectServiceRequest(request,sid):
    check(request)
    if not request.user.is_authenticated:
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Not Logged In')
        return redirect('/')
    obj = ServiceRequest.objects.get(id=sid)
    obj.status="Rejected"
    obj.save(force_update=True)
    storage = messages.get_messages(request)
    storage.used = True
    messages.info(request,f'Service Request Rejected Successfully')
    return redirect('/dadmin/dashboard')