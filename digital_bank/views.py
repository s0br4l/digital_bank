from django.core.exceptions import ObjectDoesNotExist
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
    return render(request, 'acclist.html', {'acclist': acclist})

def accid(request, acc_id):
    accid = Contas.objects.get(pk=acc_id)
    return render(request, 'acc.html', {'accid': accid})

def accbalance(request):
    return render(request, 'accbalance.html', {})

def accbalance_results(request):
    if request.method == "POST":
        searched = request.POST['searched']
        try:
            acc_searched = Contas.objects.get(cpf=searched)
            return render(request, 'accbalance_results.html',
                          {'searched': searched, 'acc_searched': acc_searched})
        except ObjectDoesNotExist:
            return render(request, 'accbalance_results.html', {})

    else:
        return render(request, 'accbalance_results.html', {})

def transactions(request):
    return render(request, 'transactions.html', {})

def acchistory(request):
    return render(request, 'acchistory.html', {})