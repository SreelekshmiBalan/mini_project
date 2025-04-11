# Generated by Django 5.2 on 2025-04-07 04:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_Name', models.CharField(max_length=500)),
                ('Category_Image', models.FileField(blank=True, null=True, upload_to='category_images/')),
                ('Category_Description', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=500)),
                ('Image', models.FileField(blank=True, null=True, upload_to='product_images/')),
                ('Price', models.IntegerField()),
                ('Description', models.CharField(max_length=2000)),
                ('Stock', models.IntegerField()),
                ('Available', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products_app.category')),
            ],
        ),
    ]
