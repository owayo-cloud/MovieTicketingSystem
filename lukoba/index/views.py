from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def contacts(request):
    return render(request, 'contacts.html', {})

def movies(request):
    return render(request, 'movies.html', {})


