from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movies', views.movies, name='movies'),
    path('contacts', views.contacts, name='contacts'),
]