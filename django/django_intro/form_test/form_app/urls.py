from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('create_users', views.create_users),
    path('success', views.success),

]