# Generated by Django 3.2.8 on 2021-10-15 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_orderitem_is_fulfilled'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='post_code',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='is_fulfilled',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('Not Yet Shipped', 'Not Yet Shipped'), ('Shipped', 'Shipped'), ('Cancelled', 'Cancelled'), ('Refunded', 'Refunded')], default='Not Yet Shipped', max_length=120),
        ),
    ]