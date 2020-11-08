from django.shortcuts import render,redirect
from student.models import Course,Enrollment
from base.models import User,StudentAnnouncement
from django.contrib import messages
# Create your views here.
def check(request):
    return request.user.user_type=="Faculty"

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
    return render(request,'facultyDashboard.html')

def facCourses(request):
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
    course = Course.objects.filter(faculty=request.user)
    return render(request,'facCourses.html',{'course':course})

def enrollment(request):
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
        student = request.POST["student"]
        course = request.POST["course"]
        Enrollment.objects.create(student=User.objects.get(first_name=student),faculty=request.user,course=Course.objects.get(name=course))
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,f'Student {student} Enrolled Successfully')
        return redirect('/faculty/dashboard')
    course = Course.objects.filter(faculty=request.user)
    students = User.objects.filter(user_type="Student")
    return render(request,'enrollStudents.html',{'students':students,'course':course})

def displayStudents(request):
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
    students = Enrollment.objects.filter(faculty=request.user)
    return render(request,'displayStudents.html',{'students':students})

def updateGrade(request):
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
        student_name = request.POST["name"]
        course = request.POST["course"]
        grade = request.POST['grade']
        Enrollment.objects.filter(faculty=request.user,course=Course.objects.get(name=course),student=User.objects.get(user_type="Student",first_name=student_name)).update(grade=grade)
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,f'Student {student_name} Grade Updated Successfully')
        return redirect('/faculty/dashboard')
    obj = Enrollment.objects.filter(faculty=request.user)
    return render(request,'updateGrade.html',{'students':obj})

def updateAttendance(request):
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
        print(request.POST)
        student_name = request.POST["name"]
        course = request.POST["course"]
        attendance = request.POST['attendance']
        Enrollment.objects.filter(faculty=request.user,course=Course.objects.get(name=course),student=User.objects.get(user_type="Student",first_name=student_name)).update(attendance=attendance)
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,f'Student {student_name} Attendance Updated Successfully')
        return redirect('/faculty/dashboard')
    obj = Enrollment.objects.filter(faculty=request.user)
    return render(request,'updateAttendance.html',{'students':obj})

def facAnnouncement(request):
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
        StudentAnnouncement.objects.create(message=message,announce_from=request.user)
    announcements = StudentAnnouncement.objects.filter(announce_from=request.user)
    return render(request,'facAnnouncement.html',{'announcements':announcements})