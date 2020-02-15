from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from .models import Book

# Create your views here.

def index (request):
    model = Book.objects.all()
    return render (request ,'booksell/home.html',{'model':model})

def about(request):
    return render (request , 'booksell/about.html')

def contact(request):
    return render(repquest , 'booksell/contact.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username , password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render (request , 'booksell/signup.html', {'form':form})