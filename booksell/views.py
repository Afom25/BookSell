from django.shortcuts import render

# Create your views here.

def index (request):
    return render (request ,'booksell/home.html')
def about(request):
    return render (request , 'booksell/about.html')