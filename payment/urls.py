from django.urls import path
from . import views

urlpatterns = [
    path('payment_sucess', views.payment_sucess, name="payment_sucess"),
    path('checkout', views.checkout, name="checkout"),
    path('billing_info', views.billing_info, name="billing_info"),
]
