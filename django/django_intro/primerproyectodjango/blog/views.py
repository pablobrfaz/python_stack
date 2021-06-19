from django.http.response import JsonResponse
from django.shortcuts import HttpResponse, redirect

def root(request):
    return redirect("/blogs")

def index(request):
    return HttpResponse("placeholder para luego mostrar una lista de todos los blogs2")

def new (request):
    return HttpResponse("placeholder para luego mostrar una lista de todos los blogs3")

def create (request):
    return HttpResponse("placeholder para luego mostrar una lista de todos los blogs4")

def show(request, my_val):	
    return HttpResponse("placeholder para mostrar el blog numero:"+str(my_val))

def edit(request, my_val):	
    return HttpResponse("placeholder para mostrar el blog numero:"+str(my_val))

def destroy(request, my_val):	
    return HttpResponse("placeholder para mostrar el blog numero:"+str(my_val))

def json(request):
    return JsonResponse({"id":"2", "curso":"valor"})