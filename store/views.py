from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required,user_passes_test
from django.utils.html import strip_tags
from django.db.models import Q
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, render

from .models import Category, Product, Service, ServiceCategory, ServiceRequests

# Create your views here.
def products_all(request):
    products = Product.products.all()

    # Note -- Probably add pagination
    context = {
        'products': products,
    }
    return render(request, 'store/products.html', context=context)

def service_all(request):
    services = Service.services.all()
    # Note -- Probably add pagination
    context = {
        'services': services,
    }
    return render(request, 'store/services.html', context=context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/product_detail.html', {'product': product})

def service_detail(request,slug):
    # Note to self -- Service should be active if product is still in stock, else not active
    service = get_object_or_404(Service, slug=slug)
    return render(request, 'store/service_detail.html', {'service': service})

def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.products.filter(categories = category)
    return render(request, 'store/category_list.html', {'category': category, 'products': products})

def service_category_list(request, category_slug=None):
    category = get_object_or_404(ServiceCategory, slug=category_slug)
    service = Service.services.filter(categories=category)
    return render(request, 'store/service_category_list.html', {'category': category, 'products': service})


@require_POST
def service_hired(request):
    service_id = request.POST.get('service_id')
    email = request.POST.get('email-address')
    phone_number = request.POST.get('phone-number')
    username= request.POST.get('username')
    address = request.POST.get('address')
    service = get_object_or_404(Service.services, id = service_id)
    vendor = service.vendor.user
    subject='You have been hired on ShopBeta'
    
    service_request = ServiceRequests.objects.create(
        user = request.user, 
        service = service,
        username = username,
        address = address,
        phone_number = phone_number,
        email = email
    )


    data = {
        'username':username,
        'email':email,
        'phone_number':phone_number,
        'hirer':request.user,
        'service_title': service.title, 
        'location': address
    }

    html_message = render_to_string('store/service-hired-email-template.html', data)

    plain_message = strip_tags(html_message)
    
    vendor.email_user(subject=subject, message = plain_message, html_message= html_message)

    return render(request, 'store/service-hired-success.html')


def search_all(request):
    query = request.GET.get('q')
    if query:
        lookups= Q(title__icontains=query) | Q(description__icontains=query)
        products = Product.products.filter(lookups)
        services = Service.services.filter(lookups)
    else:
        products = Product.products.all()
        services = Service.services.all()

    return render(request, 'store/search-results.html', {'products':products, 'services':services})