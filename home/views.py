from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'index.html', {'active_page': 'index'})


def whoweare(request):
    return render(request, 'whoweare.html', {'active_page': 'whoweare'})


def ourproduction(request):
    return render(request, 'ourproduction.html', {'active_page': 'ourproduction'})


def ourservices(request):
    return render(request, 'ourservices.html', {'active_page': 'ourservices'})


def contact(request):
    return render(request, 'contact.html', {'active_page': 'contact'})


def academy(request):
    return render(request, 'academy.html', {'active_page': 'academy'})
