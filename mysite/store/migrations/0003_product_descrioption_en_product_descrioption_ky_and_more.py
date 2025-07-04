# Generated by Django 5.2.1 on 2025-05-20 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='descrioption_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='descrioption_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='descrioption_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_name_en',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_name_ky',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_name_ru',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
