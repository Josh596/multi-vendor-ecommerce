# Generated by Django 3.2.8 on 2021-10-13 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbase',
            name='profileimage',
        ),
    ]
