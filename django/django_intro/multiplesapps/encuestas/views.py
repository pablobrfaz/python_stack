from django.shortcuts import  redirect
from django.http.response import HttpResponse

def index(request):
    return redirect("/encuestas")

def encuestas(request):
    return HttpResponse("marcador de posición para mostrar todas las encuestas creadas")

def new (request):
    return HttpResponse("marcador de posición para que los usuarios agreguen una nueva encuesta")
