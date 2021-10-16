import json
import os

import stripe
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from django.conf import settings

from pypaystack import Transaction

from basket.basket import Basket
from orders.models import Order
from orders.views import payment_confirmation

from .unique_order_key_gen import unique_order_key_generator


def order_placed(request):
    basket = Basket(request)
    order_key = request.GET.get('order_key')
    order_vendors = {} # vendor:products
    for item in basket:
        product = item['product']
        vendor = product.vendor.user

        if vendor in order_vendors:
            vendor_item = order_vendors[vendor]
            vendor_item.append(item)
        else:
            order_vendors[vendor] = [item]

    for vendor, items in order_vendors.items():

        subject='You have received a new order on ShopBeta'
        html_message = render_to_string('payment/order-placed-email-template.html',{
            'user': request.user,
            'items': items
        })

        plain_message = strip_tags(html_message)

        vendor.email_user(subject=subject, message = plain_message, html_message= html_message)

    payment_confirmation(order_key)
    basket.clear()
    return render(request, 'payment/orderplaced.html')


class Error(TemplateView):
    template_name = 'payment/error.html'


@login_required
def BasketView(request):

    basket = Basket(request)
    order_key = unique_order_key_generator()
    pk_public = settings.PAYSTACK_PUBLIC_KEY
    return render(request, 'payment/payment_form.html', {'PAYSTACK_PUBLIC_KEY':pk_public, 'basket':basket, 'order_key':order_key})


def verify(request, ref):
    transaction = Transaction(authorization_key=settings.PAYSTACK_SECRET_KEY)
    response = transaction.verify(id)
    data = JsonResponse(response, safe=False)
    payment_confirmation(ref)
    return data


@csrf_exempt
def paystack_webhook(request):

    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    # Try to validate and create a local instance of the event
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, settings.STRIPE_SIGNING_SECRET)
    except ValueError as e:
        raise e
    except stripe.error.SignatureVerificationError as e:
        raise e



    # Handle the event
    
    if event['type'] == 'payment_intent.succeeded':
        print('Payment Succeeded')

    else:
        print('Unhandled event type {}'.format(event.type))

    return HttpResponse(status=200)
