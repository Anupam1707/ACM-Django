from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('team/', views.team, name='team'),
    path('photogallery/', views.photogallery, name='photogallery'),
    
]