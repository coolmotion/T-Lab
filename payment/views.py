from django.shortcuts import render, redirect
from cart.cart import Cart
from django.contrib import messages
from django.http import HttpResponse
import json
import requests


def payment_sucess(request):
    return render(request, "payment/payment_sucess.html", {})


def checkout(request):
    return render(request, "payment/checkout.html", {})


def billing_info(request):
        shipping_info= request.session.get('shipping_info')
        print(shipping_info)
        cart = Cart(request)
        cart_products = cart.get_prods
        quantities = cart.get_quants
        totals = cart.cart_total


        return render(request, "payment/billing_info.html", {"cart_products": cart_products, "quantities": quantities, "totals": totals, "shipping_info": shipping_info})

def pay_now(request):
    # Replace these values with your actual credentials and data
    api_url = 'https://tlabstudios.lk/'
    headers = {
        'Authorization': 'xxxxxxxxxxxxxxxxx',
        'Content-Type': 'application/json'
    }
    data = {
        'amount': '202.02',
        'app_id': 'xxxxxx',
        'reference': '12345678',
        'customer_first_name': 'Johne',
        'customer_last_name': 'Dohe',
        'customer_phone_number': '+94771234567',
        'customer_email': 'onepay@spemai.com',
        'transaction_redirect_url': 'https://redirect_url',
        'additional_data': 'sample'
    }

    # Make the POST request
    response = requests.post(api_url, headers=headers, data=json.dumps(data))

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Handle the response data, maybe redirect the user or display a message
        response_data = response.json()
        # Do something with response_data
        return HttpResponse(f"Payment request successful")
    else:
        # Handle any errors, maybe log them
        print("Data:", data)
        return HttpResponse("Error: Failed to process payment request", data)