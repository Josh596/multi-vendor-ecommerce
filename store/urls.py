"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views


app_name = 'store'
urlpatterns = [
    path('', views.products_all, name='index'),
    path('services/', views.service_all, name='services'),
    path('product/detail/<slug:slug>', views.product_detail, name='product_detail'),
    path('service/detail/<slug:slug>', views.service_detail, name='service_detail'),
    path('category/<slug:category_slug>/', views.category_list, name='category_list'),
    path('search/', views.search_all, name='search'),
    path('hire/', views.service_hired, name='hire'),
    path('service-categories/<slug:category_slug>/', views.service_category_list, name='service_category_list'),
]
