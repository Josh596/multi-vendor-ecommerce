from django.contrib import admin
from .models import Category, Product, Service, ServiceCategory, ServiceRequests

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['vendor', 'title', 'slug', 'price',
                    'in_stock', 'created', 'updated']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock']
    readonly_fields = ('id','slug')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['vendor', 'title', 'slug', 'min_price','max_price',
                    'created', 'updated']
    list_filter = ['is_active']
    list_editable = ['min_price','max_price']
    readonly_fields = ('id','slug')

@admin.register(ServiceRequests)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['user','address' ,'service',]




