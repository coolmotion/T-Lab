from django.shortcuts import render


def payment_sucess(request):
    return render(request, "payment/payment_sucess.html", {})


def checkout(request):
    return render(request, "payment/checkout.html", {})


def paymenttest(request):
    data_for_payment = {
        "sandbox": True,
        "merchant_id": "1223860",
        "return_url": None,
        "cancel_url": None,
        "notify_url": "http://sample.com/notify",
        "order_id": "ItemNo12345",
        "items": "Door bell wireless",
        "amount": "1000.00",
        "currency": "LKR",
        "hash": "45D3CBA93E9F2189BD630ADFE19AA6DC",
        "first_name": "Saman",
        "last_name": "Perera",
        "email": "samanp@gmail.com",
        "phone": "0771234567",
        "address": "No.1, Galle Road",
        "city": "Colombo",
        "country": "Sri Lanka",
        "delivery_address": "No. 46, Galle road, Kalutara South",
        "delivery_city": "Kalutara",
        "delivery_country": "Sri Lanka",
        "custom_1": "",
        "custom_2": ""
    }
    return render(request, "payment/ptest.html", {'payment_data': data_for_payment})
