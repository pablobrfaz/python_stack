from django.shortcuts import  redirect
from django.http.response import HttpResponse

def index1(request):
    return redirect("/register")

def encuestas(request):
    return HttpResponse("marcador de posición para que los usuarios creen un nuevo registro de usuario")

def login(request):
    return HttpResponse("marcador de posición para que los usuarios inicien sesión")

def usuarios(request):
    return HttpResponse("marcador de posición para luego mostrar toda la lista de usuarios")

def new (request):
    return HttpResponse("marcador de posición para que los usuarios agreguen una nueva encuesta")
