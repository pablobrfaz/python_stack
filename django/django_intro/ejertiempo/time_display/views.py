from django.shortcuts import render
from time import localtime, strftime

def index(request):
    context = {
        "time": strftime('Mes: %m, %Y, Hora: %H, Minutos: %M', localtime())
    }
    return render(request,'index.html', context)