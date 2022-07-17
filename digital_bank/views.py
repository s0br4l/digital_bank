from django.shortcuts import render
from .forms import NewAccForm
from django.http import HttpResponseRedirect
from .models import Contas, Historico

def home(request):
    return render(request, 'home.html', {})

def newacc(request):
    submitted = False
    if request.method == "POST":
        form = NewAccForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/newacc?submitted=True')
    else:
        form = NewAccForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'newacc.html', {'form': form, 'submitted': submitted})


def acclist(request):
    acclist = Contas.objects.all()
    return render(request, 'acclist.html', {'acclist':acclist})

def accbalance(request):
    return render(request, 'accbalance.html', {})

def transactions(request):
    return render(request, 'transactions.html', {})

def acchistory(request):
    return render(request, 'acchistory.html', {})