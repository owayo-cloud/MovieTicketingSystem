from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def contacts(request):
    return render(request, 'contacts.html', {})

def movies(request):
    return render(request, 'movies.html', {})

def dashboard(request):
    return render(request, 'dashboard.html', {})

def dashboardMovies(request):
    return render(request, 'dashboard_movies.html', {})

def dashboardBookings(request):
    return render(request, 'dashboard_bookings.html', {})

def dashboardUsers(request):
    return render(request, 'dashboard_users.html', {})

