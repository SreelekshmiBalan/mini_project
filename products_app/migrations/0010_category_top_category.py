# Generated by Django 5.2 on 2025-04-09 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0009_product_colour'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='Top_Category',
            field=models.BooleanField(default=False),
        ),
    ]
