from django.http.response import JsonResponse
from django.shortcuts import render

from basket.basket import Basket


from .models import Order, OrderItem


def add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':

        order_key = request.POST.get('order_key')
        address = request.POST.get('address')
        address2 = request.POST.get('address2', None)
        user_id = request.user.id
        baskettotal = basket.get_total_price()
        baskettotal = baskettotal

        # Check if product is still in stock
        # Check if order exists
        if Order.objects.filter(order_key=order_key).exists():
            pass
        else:
            order = Order.objects.create(user_id=user_id, full_name='name', address1=address,
                                address2=address2, total_paid=baskettotal, order_key=order_key)
            for item in basket:
                item = OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['qty'], status = 1)
            
        response = JsonResponse({'success': 'Return something'})
        return response



def payment_confirmation(data):
    Order.objects.filter(order_key=data).update(billing_status=True)


def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders