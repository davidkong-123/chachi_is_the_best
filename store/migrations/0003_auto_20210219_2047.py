# Generated by Django 3.1.5 on 2021-02-20 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='prodct',
            new_name='product',
        ),
    ]
