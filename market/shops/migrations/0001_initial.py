# Generated by Django 4.2 on 2023-07-13 12:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='banners/')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=False)),
                ('link', models.CharField(blank=True)),
            ],
            options={
                'verbose_name': 'баннер',
                'verbose_name_plural': 'баннеры',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='обновлено')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='цена')),
                ('in_stock', models.IntegerField(blank=True, default=0, verbose_name='наличие')),
                ('limited_edition', models.BooleanField(default=True, verbose_name='ограниченное предложение')),
                ('index', models.IntegerField(default=0, verbose_name='индекс сортировки')),
            ],
            options={
                'verbose_name': 'предложение',
                'verbose_name_plural': 'предложения',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание магазина')),
                ('phone_number', models.CharField(blank=True, max_length=18, null=True, validators=[django.core.validators.RegexValidator(message="Номер телефона должен быть введен в формате: '+7 (123) 456-78-90'. Максимальная длина 12 символов.", regex='^\\+\\d{1,3}\\s\\(\\d{3}\\)\\s\\d{3}-\\d{2}-\\d{2}$')], verbose_name='номер телефона')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='адрес')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='email')),
                ('products', models.ManyToManyField(related_name='shops', through='shops.Offer', to='products.product', verbose_name='товары в магазине')),
            ],
            options={
                'verbose_name': 'магазин',
                'verbose_name_plural': 'магазины',
            },
        ),
    ]
