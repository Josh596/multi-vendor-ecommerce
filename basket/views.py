from datetime import datetime, timedelta
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.conf import settings
from store.models import Product

from .basket import Basket


def get_total_qty(request):
    basket = Basket(request)

    basketqty = basket.__len__()
    
    return basketqty

def get_total_price(request):
    basket = Basket(request)
    basketprice = basket.get_total_price()
    
    return basketprice

def get_subtotal_price(request):
    basket = Basket(request)
    basketprice = basket.get_subtotal_price()
    
    return basketprice

def basket_summary(request):
    basket = Basket(request)
    return render(request, 'basket/cart.html', {'basket': basket})


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)

        basketqty = get_total_qty(request)
        response = JsonResponse({'qty': basketqty})
        return response





def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)

        basketqty = get_total_qty(request)
        baskettotal = basket.get_total_price()
        basketsubtotal = basket.get_subtotal_price()
        response = JsonResponse({'qty': basketqty, 'total': baskettotal, 'subtotal':basketsubtotal})
        return response



def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        basket.update(product=product_id, qty=product_qty)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        basketsubtotal = basket.get_subtotal_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': basketsubtotal, 'total':baskettotal})
        return response

