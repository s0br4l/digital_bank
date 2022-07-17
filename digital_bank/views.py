from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def newacc(request):
    return render(request, 'newacc.html', {})

def acclist(request):
    return render(request, 'acclist.html', {})

def accbalance(request):
    return render(request, 'accbalance.html', {})

def transactions(request):
    return render(request, 'transactions.html', {})

def acchistory(request):
    return render(request, 'acchistory.html', {})