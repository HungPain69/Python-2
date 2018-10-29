from django.urls import path

from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('product', views.productList.as_view(
        template_name ='app/productList.html'
    ), name= 'productList'),
    path('product/<int:pk>', views.productDetail.as_view(
        template_name = 'app/productDetail.html'), name= 'productDetail'),

    path('order', views.orderList.as_view(
        template_name ='app/orderList.html'), name = 'orderList'),
    
    path('order/<int:pk>', views.orderDetail.as_view(
        template_name= 'app/orderDetail.html'), name = 'orderDetail'),

    path('customer', views.customerList.as_view(
        template_name ='app/customerList.html'), name = 'customerList'),

    path('customer/<pk>', views.customerDetail.as_view(
        template_name= 'app/customerDetail.html'), name = 'customerDetail'),
]