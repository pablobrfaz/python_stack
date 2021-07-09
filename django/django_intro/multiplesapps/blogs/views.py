from django.shortcuts import  redirect
from django.http.response import HttpResponse

def index(request):
    return redirect("/blogs")

def blogs(request):
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
