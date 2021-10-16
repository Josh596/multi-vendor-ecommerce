from random import randint
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify 
from account.models import UserBase
from vendor.models import Vendor



class ProductManager(models.Manager):
	def get_queryset(self):
		return super(ProductManager, self).get_queryset().filter(is_active=True, in_stock=True)

class ServiceManager(models.Manager):
	def get_queryset(self):
		return super(ServiceManager, self).get_queryset().filter(is_active=True)



class Category(models.Model):
	name = models.CharField(max_length=255, db_index=True)
	slug = models.SlugField(max_length=255, unique=True)
	icon = models.CharField(max_length=255,
		default='fa fa-list-alt', 
		help_text='Font Awesome or Bootstrap class [https://fontawesome.com/v5.15/icons?d=gallery&p=2&m=free][https://icons.getbootstrap.com/](e.g, fa fa-shopping-cart)')
	class Meta:
		verbose_name_plural = 'categories'

	def get_absolute_url(self):
		return reverse('store:category_list', args=[self.slug])

	def __str__(self):
		return self.name

class ServiceCategory(models.Model):
	name = models.CharField(max_length=255, db_index=True)
	slug = models.SlugField(max_length=255, unique=True)
	icon = models.CharField(max_length=255,
		default='fa fa-list-alt', 
		help_text='Font Awesome or Bootstrap class [https://fontawesome.com/v5.15/icons?d=gallery&p=2&m=free][https://icons.getbootstrap.com/](e.g, fa fa-shopping-cart)')
	class Meta:
		verbose_name_plural = 'Service Categories'

	def get_absolute_url(self):
		return reverse('store:service_category_list', args=[self.slug])




class Product(models.Model):
	categories = models.ManyToManyField(Category, related_name='%(app_label)s_%(class)s_related', blank=True)
	vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_related')
	title = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to='images/', default='images/default.jpg')
	slug = models.SlugField(max_length=50, null=True, blank=True)
	price = models.IntegerField()
	in_stock = models.BooleanField(default=True)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	products = ProductManager()
	objects = models.Manager()

	class Meta:
		verbose_name_plural = 'Products'
		ordering = ('-created',)

	def save(self, *args, **kwargs):
		if Product.objects.filter(title=self.title).exists():
			extra = str(randint(1, 10000))
			self.slug = slugify(self.title) + "-" + extra
		else:
			self.slug = slugify(self.title)
		super(Product, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('store:product_detail', args=[self.slug])

	def __str__(self):
		return self.title

class Service(models.Model):
	categories = models.ManyToManyField(ServiceCategory, related_name='%(app_label)s_%(class)s_related', blank=True)
	vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_related', null=True, blank=True)
	title = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to='images/store', default='images/default.jpg')
	slug = models.SlugField(max_length=50, null=True, blank=True)
	min_price = models.IntegerField()
	max_price = models.IntegerField()
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	services = ServiceManager()
	objects = models.Manager()

	class Meta:
		verbose_name_plural = 'Services'
		ordering = ('-created',)

	def save(self, *args, **kwargs):
		if Service.objects.filter(title=self.title).exists():
			extra = str(randint(1, 10000))
			self.slug = slugify(self.title) + "-" + extra
		else:
			self.slug = slugify(self.title)
		super(Service, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('store:service_detail', args=[self.slug])

	def __str__(self):
		return self.title


class ServiceRequests(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_related', null=True)
	service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_related')
	username = models.CharField(max_length=250)
	address = models.TextField()
	phone_number = models.CharField(max_length=16)
	email = models.EmailField()
	created = models.DateTimeField(auto_now_add=True)
	
