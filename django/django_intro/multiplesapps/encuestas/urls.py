from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index2),
    path('encuestas', views.encuestas),
    path('encuestas/new',views.new),
]