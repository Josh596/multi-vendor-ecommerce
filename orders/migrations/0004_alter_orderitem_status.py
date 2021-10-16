# Generated by Django 3.2.8 on 2021-10-16 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20211015_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Not Yet Shipped'), (2, 'Shipped'), (3, 'Cancelled'), (4, 'Refunded')], default=1),
        ),
    ]