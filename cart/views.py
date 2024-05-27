from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from payment.froms import ShippingForm
from django.contrib import messages


def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()
    if request.method == 'POST':
        shipping_form = ShippingForm(request.POST)
        if shipping_form.is_valid():
            shipping_info = shipping_form.cleaned_data
            request.session['shipping_info'] = shipping_info
            return redirect('billing_info')
        else:
            messages.success(request, "Please check your shipping info")
    else:
        shipping_form = ShippingForm()
    return render(request, "cart_summary.html", {
        "cart_products": cart_products,
        "quantities": quantities,
        "total": totals,
        "shipping_form": shipping_form
    })



def cart_add(request):

    cart = Cart(request)

    if request.POST.get('action') == 'post':

        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        product = get_object_or_404(Product, id=product_id)

        cart.add(product=product, quantity=product_qty)

        cart_quantity = cart.__len__()

        response = JsonResponse({'qty': cart_quantity})
        return response


def cart_delete(render):
    pass


def cart_update(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':

        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id, quantity=product_qty)

        response = JsonResponse({'qty': product_qty})
        return response
