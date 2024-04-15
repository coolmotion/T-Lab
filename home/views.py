from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, 'index.html')


def whoweare(request):
    return render(request, 'whoweare.html')


def ourproduction(request):
    return render(request, 'ourproduction.html')


def ourservices(request):
    return render(request, 'ourservices.html')


def contact(request):
    return render(request, 'contact.html')


def academy(request):
    return render(request, 'academy.html')
