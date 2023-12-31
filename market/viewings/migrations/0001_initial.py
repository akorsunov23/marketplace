# Generated by Django 4.2 on 2023-07-13 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistorySearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'история просмотров',
                'verbose_name_plural': 'история просмотров',
            },
        ),
        migrations.CreateModel(
            name='HistorySearchProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='дата')),
                ('history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history_products', to='viewings.historysearch', verbose_name='история')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history_products', to='products.product', verbose_name='продукт')),
            ],
            options={
                'verbose_name': 'история просмотра продукта',
                'verbose_name_plural': 'история просмотра продуктов',
            },
        ),
        migrations.AddField(
            model_name='historysearch',
            name='product',
            field=models.ManyToManyField(related_name='history', through='viewings.HistorySearchProduct', to='products.product', verbose_name='продукт'),
        ),
        migrations.AddField(
            model_name='historysearch',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
    ]
