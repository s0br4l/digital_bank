from decimal import Decimal
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from .forms import NewAccForm
from django.http import HttpResponseRedirect
from .models import Contas, Transferencias


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


def transactions_results(request):
    if request.method == "POST":
        cpfenvia = request.POST['envia']
        cpfrecebe = request.POST['recebe']
        data_transf = request.POST['data']
        try:
            valor_transf = float(request.POST['valor'])
            valor_envia = Decimal(valor_transf * (-1))
            valor_recebe = Decimal(valor_transf)
        except ValueError:
            return render(request, 'transactions_results.html', {})

        try:
            acc_envia = Contas.objects.get(cpf=cpfenvia)
            acc_envia.saldo = acc_envia.saldo + valor_envia
            acc_envia.save()
            acc_recebe = Contas.objects.get(cpf=cpfrecebe)
            acc_recebe.saldo = acc_recebe.saldo + valor_recebe
            acc_recebe.save()
            return render(request, 'transactions_results.html',
                          {'cpfenvia': cpfenvia, 'cpfrecebe': cpfrecebe,'valor_envia': valor_envia,
                           'valor_recebe': valor_recebe,'data_transf': data_transf,
                           'acc_envia': acc_envia,'acc_recebe': acc_recebe})
        except ObjectDoesNotExist:
            return render(request, 'transactions_results.html', {'valor_transf': valor_transf})

    else:
        return render(request, 'transactions_results.html', {})


def acchistory(request):
    return render(request, 'acchistory.html', {})
