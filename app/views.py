from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from django.views.generic import TemplateView,DeleteView,ListView, DetailView

from .models import Products, Categories, Customers, Order


class index(TemplateView):
    template_name ='app/index.html'

class productList(ListView):
    model= Products
    context_object_name = 'product_list'
    
    def get_queryset(self):
        return Products.objects.all()

class productDetail(DetailView):
    context_object_name = 'product'
    model = Products
    queryset = Products.objects.all()


class orderList(ListView):
    model = Order
    context_object_name= 'order_list'
    def get_queryset(self):
        return Order.objects.all()


class orderDetail(DetailView):
    context_object_name ='order'
    model = Order
    queryset= Order.objects.all()    


class customerList(ListView):
    model = Customers
    context_object_name= 'customer_list'
    def get_queryset(self):
        return Customers.objects.all()

class customerDetail(DetailView):
    context_object_name ='customer'
    model = Customers
    queryset= Customers.objects.all() 