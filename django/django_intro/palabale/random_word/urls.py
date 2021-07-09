from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('palabra_random', views.palabra_random),
    path('reset',views.reset),
]