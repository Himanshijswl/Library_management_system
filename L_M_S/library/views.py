from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Create your views here.
def index(request):
    return render(request,'index.html')

def view_book(request):
    bs = Book.objects.all()
    context={
        'bs':bs
    }
    print(context)
    return render(request,'view_book.html', context)

def add_book(request):
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        price = int(request.POST['price'])
        author = int(request.POST['author'])
        new_book = Book(name= name, subject = subject, price = price, author_id = author)
        new_book.save()
        return HttpResponse("Book added successfully!")
    elif request.method == 'GET':
        return render(request,'add_book.html')
    else:
        return HttpResponse("An exception occurred! Book has not been added")

def update_book(request):
    return render(request,'update_book.html')

def delete_book(request, b_id = 0):
    if b_id:
        try:
            book_to_be_removed = Book.objects.get(id= b_id)
            book_to_be_removed.delete()
            return HttpResponse("Book deleted successfully!")
        except:
            return HttpResponse("Please enter a valid Book ID")
    bs = Book.objects.all()
    context = {
        'bs': bs
    }
    return render(request,'delete_book.html', context)

def filter_book(request):
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        price = request.POST['price']
        author = request.POST['author']
        bs = Book.objects.all()

        if name:
            bs = bs.filter(Q(name__icontains = name))
        if subject:
            bs = bs.filter(subject__name__icontains = subject)
        if price:
            bs = bs.filter(price__value__icontains = price)
        if author:
            bs = bs.filter(author__name = author)

        context ={
            'bs': bs
        }

        return render(request,'view_book.html', context)
        
    elif request.method == 'GET':
        return render(request,'filter_book.html')
    else:
        return HttpResponse('An Exception occurred!')

def home(request):
    return render(request, "home.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request, "Your Account has been successfully created")
        return redirect('signin')

    return render(request, "signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username= username, password = pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'index.html', {'fname': fname})
        else:
            messages.error(request, "Wrong Credentials")
            return redirect('home')


    return render(request, "signin.html")

def signout(request):
    pass