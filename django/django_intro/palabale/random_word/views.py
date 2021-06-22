from django.shortcuts import render
from django.utils.crypto import get_random_string

def index(request):
    context = {
        "get_random_string": get_random_string(length=14),
        
    }
    return render(request,'index.html', context)


