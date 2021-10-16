from django.contrib import admin

from .models import Order, OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','total_paid', 'billing_status', 'created', 'updated']
    readonly_fields = ()

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'price', 'quantity', 'status', 'created', 'updated']
    readonly_fields = ('product', 'price', 'quantity')

