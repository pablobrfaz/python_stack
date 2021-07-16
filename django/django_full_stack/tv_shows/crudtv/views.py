from django.shortcuts import render, redirect
from .models import showtv
from django.contrib import messages
from django.db.models.expressions import Value

def index(request):
    return redirect("/shows")

# View para llamar a toda la lista de la base de datos
def read_all(request):
    context = {
        'shows_tot' : showtv.objects.all()
    }

    return render(request, "mostrar.html", context)

# View para llevar a la pagina 
def nuevo_show(request):
    return render(request, 'nuevoshow.html')

def crear_show(request):
    errors = showtv.objects.form_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/shows/new')
    else:
        nuevo_show = showtv.objects.create(
                title = request.POST['titleInput'],
                network = request.POST['networkInput'],
                release_date = request.POST['dateInput'],
                description = request.POST['descriptionInput'],
            )
        context = {
                'nuevo_show' : nuevo_show
            }
        return render(request, 'mostrar_show.html',context)

def read_show(request,number):
    nuevo_show = showtv.objects.get(id=number)
    context = {
        'nuevo_show' : nuevo_show
    }
    return render(request, 'mostrar_show.html',context)

def borrar_show(request,number):
    borr_show = showtv.objects.get(id=number)
    borr_show.delete()
    return redirect('/shows')

def edit_show(request,number):
    if request.method == "POST":
        errors = showtv.objects.form_validator(request.POST)
        if len(errors) > 0:
            edit_show = showtv.objects.get(id=number)
            context = {
                    'nuevo_show' : edit_show
            }
            for key, value in errors.items():
                messages.error(request,value)
            context['up_date']= str(context['nuevo_show'].release_date)
            return render(request, 'modificar.html',context)
        else:
            update_show = showtv.objects.get(id=request.POST['show_id'])
            update_show.title = request.POST['titleInput']
            update_show.network = request.POST['networkInput']
            update_show.release_date = request.POST['dateInput']
            update_show.description = request.POST['descriptionInput']
            update_show.save()
            context = {
                'nuevo_show' : update_show
            }
            return render(request, 'mostrar_show.html',context)
    edit_show = showtv.objects.get(id=number)
    context = {
        'nuevo_show' : edit_show
        }
    context['up_date']= str(context['nuevo_show'].release_date)
    return render(request, 'modificar.html',context)
