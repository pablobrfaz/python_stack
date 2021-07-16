from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('shows',views.read_all),	 
    path('shows/new', views.nuevo_show),
    path('shows/create', views.crear_show),
    path('shows/<int:number>', views.read_show),
    path('shows/<int:number>/delete',views.borrar_show),
    path('shows/<int:number>/edit', views.edit_show),
    path('shows/update/<int:number>',views.edit_show),
]