from django.shortcuts import render, redirect
from cart.cart import Cart
from django.contrib import messages


def payment_sucess(request):
    return render(request, "payment/payment_sucess.html", {})


def checkout(request):
    return render(request, "payment/checkout.html", {})


def billing_info(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prods
        quantities = cart.get_quants
        totals = cart.cart_total

        return render(request, "payment/billing_info.html", {"cart_products": cart_products, "quantities": quantities, "totals": totals, "shipping_info": request.POST})
    else:
        messages.success(request, "Access Denied")
        return redirect('shop')
