from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movies, name='movies'),
    path('contacts/', views.contacts, name='contacts'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/movies/', views.dashboardMovies, name='dashboard_movies'),
    path('dashboard/bookings/', views.dashboardBookings, name='dashboard_bookings'),
    path('dashboard/users/', views.dashboardUsers, name='dashboard_users'),
]