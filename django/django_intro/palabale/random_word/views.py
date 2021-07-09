from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from django.http.response import HttpResponse

def index(request):
    return redirect("/palabra_random")

def palabra_random(request):
    context = {
        "get_random_string": get_random_string(length=14),
        
    }
    if 'count' not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1

    return render(request,'index.html', context)


def reset(request):
    request.session.clear()
    return render(request,"index.html")