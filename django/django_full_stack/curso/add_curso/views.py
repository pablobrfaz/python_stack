from django.shortcuts import render, redirect
from .models import curso, description
from django.contrib import messages

# Create your views here.

def index(request):
    context = {
                'all_courses' : curso.objects.all(),
                'all_descriptions' : curso.objects.all()
            }
    return render(request,'add_view.html',context)

def add_cursos(request):
    errors = curso.objects.curso_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/')
    else:
        if request.method == "POST":
            nuevo_curso = curso.objects.create(nombre = request.POST['nombre'],)
            description.objects.create(description = request.POST['description'],Curso = nuevo_curso)
        return redirect('/')

def del_cursos(request,number):
    if request.method == "POST":
        if request.POST['confirm'] == "No":
            return redirect('/')
        else:
            del_course = curso.objects.get(id=number)
            del_course.delete()
            return redirect('/')
    context = {
        'del_course' : curso.objects.get(id=number)
    }
    return render(request,'borrar.html',context)

