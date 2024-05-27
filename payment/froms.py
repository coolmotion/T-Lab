from django import forms
from .models import ShippingAddress


class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': "block my-3 w-full rounded-xl lg:px-3  border-0 px-4 py-2 text-gray-300 px-4 placeholder:text-gray-400 bg-zinc-900 sm:text-sm sm:leading-6 ", 'placeholder': "Full Name"}), required=False)
    shipping_email = forms.EmailField(label="", widget=forms.TextInput(
        attrs={'class': "block my-3 w-full rounded-xl lg:px-3  border-0 px-4 py-2 text-gray-300 px-4 placeholder:text-gray-400 bg-zinc-900 sm:text-sm sm:leading-6", 'placeholder': "Email"}), required=False)
    shipping_address1 = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': "block my-3 w-full rounded-xl lg:px-3  border-0 px-4 py-2 text-gray-300 px-4 placeholder:text-gray-400 bg-zinc-900 sm:text-sm sm:leading-6", 'placeholder': "Address Line 1"}), required=False)
    shipping_address2 = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': "block my-3 w-full rounded-xl lg:px-3  border-0 px-4 py-2 text-gray-300 px-4 placeholder:text-gray-400 bg-zinc-900 sm:text-sm sm:leading-6", 'placeholder': "Address Line 2"}), required=False)
    shipping_city = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': "block my-3 w-full rounded-xl lg:px-3  border-0 px-4 py-2 text-gray-300 px-4 placeholder:text-gray-400 bg-zinc-900 sm:text-sm sm:leading-6", 'placeholder': "City"}), required=False)
    shipping_zipcode = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': "block my-3 w-full rounded-xl lg:px-3  border-0 px-4 py-2 text-gray-300 px-4 placeholder:text-gray-400 bg-zinc-900 sm:text-sm sm:leading-6", 'placeholder': "Zip Code"}), required=False)

    class Meta:
        model = ShippingAddress
        fields = ['shipping_full_name', 'shipping_email', 'shipping_address1',
                  'shipping_address2', 'shipping_city', 'shipping_zipcode']

        exlude = ['user',]
