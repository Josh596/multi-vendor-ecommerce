# Generated by Django 3.2.8 on 2021-10-12 19:11

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('category_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='store.category')),
            ],
            options={
                'verbose_name_plural': 'Service Categories',
            },
            bases=('store.category',),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(default='admin', max_length=255)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(default='images/default.png', upload_to='images/')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('price', models.IntegerField()),
                ('in_stock', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(related_name='readable_store_product_related', to='store.Category')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='readable_store_product_related', to='vendor.vendor')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ('-created',),
            },
            managers=[
                ('products', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(default='images/default.png', upload_to='images/store')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('price', models.IntegerField()),
                ('in_stock', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='readable_store_service_related', to='vendor.vendor')),
                ('categories', models.ManyToManyField(related_name='readable_store_service_related', to='store.ServiceCategory')),
            ],
            options={
                'verbose_name_plural': 'Services',
                'ordering': ('-created',),
            },
            managers=[
                ('services', django.db.models.manager.Manager()),
            ],
        ),
    ]
