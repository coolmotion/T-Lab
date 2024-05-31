from django.shortcuts import render, redirect
from cart.cart import Cart
from django.contrib import messages
from django.http import HttpResponse
import json


def payment_sucess(request):
    return render(request, "payment/payment_sucess.html", {})


def checkout(request):
    return render(request, "payment/checkout.html", {})


def billing_info(request):
    shipping_info = request.session.get('shipping_info')
    print(shipping_info)
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total

    return render(request, "payment/billing_info.html", {"cart_products": cart_products, "quantities": quantities, "totals": totals, "shipping_info": shipping_info})
