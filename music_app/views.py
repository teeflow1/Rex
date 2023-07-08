from django.shortcuts import render

def home(request):
    return render(request, 'apps/home.html', {})

def ticket(request):
    return render(request, 'apps/ticket.html', {})
