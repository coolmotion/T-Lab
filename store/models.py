from django.db import models
from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    # Change EmailField to CharField
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Product(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(
        max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')
    is_rent =models.BooleanField(default=False)
    rent_per_week=models.DecimalField(default=0, decimal_places=2, max_digits=10)
    rent_per_month=models.DecimalField(default=0, decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=10, default='',
                             blank=True)
    date = models.DateField(default=datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.product)
