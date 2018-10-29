from django.contrib import admin

from .models import Products, Categories, Customers, Order, OrderItem, DeliveryAddresses, Logins


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name","description"]
    search_fields = ["name"]
    list_filter = ["name"]

admin.site.register(Products,ProductAdmin)
admin.site.register(Categories)
admin.site.register(Customers)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(DeliveryAddresses)
admin.site.register(Logins)
