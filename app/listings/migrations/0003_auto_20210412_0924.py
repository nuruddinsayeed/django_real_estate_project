# Generated by Django 3.1.8 on 2021-04-12 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20210412_0858'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='pricce',
            new_name='price',
        ),
    ]
