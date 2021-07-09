from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('register',views.register),
    path('login',views.login),
    path('usuarios/',views.usuarios),
    path('usuarios/new',views.new),
    
]
