from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),	 
    path('books/<int:number>',views.books),
    path('authors/',views.IndexAuthors),
    path('authors/<int:number>',views.authors),
]