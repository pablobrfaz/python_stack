from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('encuestas', views.encuestas),
    path('encuestas/new',views.new),
]