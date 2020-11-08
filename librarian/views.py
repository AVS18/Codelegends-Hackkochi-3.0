from django.shortcuts import render,redirect
from base.models import StudentAnnouncement,User
from .models import Book,BookRequest
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def check(request):
    return request.user.user_type=="Librarian"

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
    return render(request,'libraryDashboard.html')
def addBook(request):
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
        name = request.POST["name"]
        author = request.POST["author"]
        no_of_copies = request.POST["no_of_copies"]
        Book.objects.create(name=name,author=author,no_of_copies=no_of_copies)
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,f'Book {name} added successfully')
        return redirect('/librarian/dashboard')
    books = Book.objects.all()
    return render(request,'addBook.html',{'books':books})
def bookrequest(request):
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
    requests = BookRequest.objects.filter(status="Pending")
    all_request = BookRequest.objects.all()
    return render(request,'bookRequest.html',{'book_request':requests,'all_request':all_request})

def acceptBookRequest(request,bid):
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
    obj = BookRequest.objects.get(id=bid)
    obj2 = Book.objects.get(name=obj.book.name)
    obj2.no_of_copies =obj2.no_of_copies-1
    obj.status="Accepted"
    obj2.save(force_update=True) 
    obj.save(force_update=True)
    storage = messages.get_messages(request)
    storage.used = True
    messages.info(request,f'Request Accepted Successfully')
    return redirect('/librarian/dashboard')

def rejectBookRequest(request,bid):
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
    obj = BookRequest.objects.get(id=bid)
    obj.status="Rejected"
    obj.save(force_update=True)
    storage = messages.get_messages(request)
    storage.used = True
    messages.info(request,f'Request Rejected Successfully')
    return redirect('/librarian/dashboard')

def alertUser(request):
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
        name = request.POST["name"]
        obj = User.objects.get(id=name)
        name,email = obj.first_name,obj.email
        message = request.POST["message"]
        msg = 'Respected '+name+',\n\n\t'+message
        send_mail("Hack Kochi 3.0",msg,from_email='adityaintern11@gmail.com',recipient_list=[email])
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,f'Email Sent Successfully')
        return redirect('/librarian/dashboard')
    obj = User.objects.filter(user_type="Student")
    return render(request,'sendmail.html',{'obj':obj})
def makeAnnouncement(request):
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
    return render(request,'libAnnouncement.html',{'announcements':announcements})
