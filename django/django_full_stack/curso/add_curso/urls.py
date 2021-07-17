from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('add_cursos/',views.add_cursos),
    path('delet_cursos/<int:number>',views.del_cursos),

    ]	 