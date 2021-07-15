from django.shortcuts import render, redirect
from datetime import datetime
import random

def index(request):
    if 'agregar_oro' not in request.session or 'activities' not in request.session:
        request.session['agregar_oro'] = 0
        request.session['activities'] = ""
    return render(request,'index.html')

def process_money(request):
    if request.method == "POST":
        if request.POST['tipo_oro'] == 'farm':
            random_gold = random.randint(10, 21)
            request.session['activities']  += '\nEarned ' + str(random_gold) + ' golds from the Farm! ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')' 
        elif request.POST['tipo_oro'] == 'cave':
            random_gold = random.randint(5, 11)
            request.session['activities'] += '\nEarned ' + str(random_gold) + ' golds from the Cave ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')'
        elif request.POST['tipo_oro'] == 'house':
            random_gold = random.randint(2,6)
            request.session['activities'] += '\nEarned ' + str(random_gold) + ' golds from the House ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')'
        elif request.POST['tipo_oro'] == 'casino':
            random_gold = random.randint(-50, 51)
            if random_gold >= 0:
                request.session['activities'] += '\nEntered a Casino and won ' + str(random_gold) +' golds' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')'
            else:
                request.session['activities'] += '\nEntered a Casino and lost ' + str(random_gold) + ' golds... Ouch...' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')'
        request.session['agregar_oro'] += random_gold
    
    return render(request,"index.html")

def reset(request):
    request.session.clear()
    return redirect("/")