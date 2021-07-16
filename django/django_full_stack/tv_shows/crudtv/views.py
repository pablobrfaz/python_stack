from django.shortcuts import render, redirect
from .models import showtv

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
    edit_show = showtv.objects.get(id=number)
    context = {
        'new_show' : edit_show
        }
    context['up_date']= str(context['new_show'].release_date)
    return render(request, 'modificar.html',context)
