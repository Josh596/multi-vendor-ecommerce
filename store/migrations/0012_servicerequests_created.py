# Generated by Django 3.2.8 on 2021-10-16 16:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20211016_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequests',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]