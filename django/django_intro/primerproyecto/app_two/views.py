from django.shortcuts import render, HttpResponse

def first_view(request):
    return HttpResponse("Esta es la primera vista de la app2")

def second_view(request):
    return HttpResponse("Esta es la Segunda vista de la app2")