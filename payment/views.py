from django.shortcuts import render


def payment_sucess(request):
    return render(request, "payment/payment_sucess.html", {})


def checkout(request):
    return render(request, "payment/checkout.html", {})
