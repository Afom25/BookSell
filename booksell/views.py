from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from .models import Book,History,Fiction

# Create your views here.

def index (request):
    model = Book.objects.all()
    return render (request ,'booksell/home.html',{'model':model})
def history(request):
    modelhistory = History.objects.all()
    return render (request, 'booksell/history.html',{'modelhistory':modelhistory})
def fiction(request):
    modelfiction = Fiction.objects.all()
    return render (request, 'booksell/fiction.html', {'modelfiction':modelfiction})
def details(request):
    model = Book.objects.all()
    return render (request ,'booksell/details.html',{'model':model})
    

def about(request):
    return render (request , 'booksell/about.html')

def contact(request):
    return render(request , 'booksell/contact.html')

def search_results(request):
    if 'book' in request.GET and request.GET["book"]:
        search_term = request.GEt.get("shareit")
        searched_image = Book.search_by_title(earch_term)
        message = f"{search_term}"
        
        return render(request,'booksell/search.html', {"message":message,"book":searched_image})
    else:
        message = "You haven't searched for any term"
        
        return render(request, 'booksell/serach.html',{"message"})

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