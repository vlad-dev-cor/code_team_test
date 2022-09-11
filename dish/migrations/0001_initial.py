# Generated by Django 4.0.5 on 2022-09-07 20:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='идентификатор')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name_ru', models.CharField(max_length=255, unique=True, verbose_name='Название на русском')),
                ('name_en', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Название на английском')),
                ('name_ch', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Название на китайском')),
                ('order_id', models.SmallIntegerField(blank=True, default=10, null=True)),
            ],
            options={
                'verbose_name': 'Раздел меню',
                'verbose_name_plural': 'Разделы меню',
                'ordering': ('name_ru', 'order_id'),
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='идентификатор')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_vegan', models.BooleanField(default=False, verbose_name='Вегетарианское меню')),
                ('is_special', models.BooleanField(default=False, verbose_name='Специальное предложение')),
                ('code', models.IntegerField(verbose_name='Код поставщика')),
                ('internal_code', models.IntegerField(blank=True, null=True, unique=True, verbose_name='Код в приложении')),
                ('name_ru', models.CharField(max_length=255, verbose_name='Название на русском')),
                ('description_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание на русском')),
                ('description_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание на английском')),
                ('description_ch', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание на китайском')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('is_publish', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('additional', models.ManyToManyField(blank=True, related_name='additional_from', to='dish.food', verbose_name='Дополнительные товары')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food', to='dish.foodcategory', verbose_name='Раздел меню')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
