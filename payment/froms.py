from django import forms
from models import ShippingAddress


class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "Full Name"}), required=False)
    shipping_email = forms.EmailField(label="", widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "Email"}), required=False)
    shipping_address1 = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "Address Line 1"}), required=False)
    shipping_address2 = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "Address Line 2"}), required=False)
    shipping_city = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "City"}), required=False)
    shipping_zipcode = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "Zip Code"}), required=False)

    class Meta:
        model = ShippingAddress
        fields = ['shipping_full_name', 'shipping_email', 'shipping_address1',
                  'shipping_address2', 'shipping_city', 'shipping_zipcode']

        exlude = ['user',]
