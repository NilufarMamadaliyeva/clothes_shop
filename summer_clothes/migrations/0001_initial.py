# Generated by Django 5.0.1 on 2024-02-03 05:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewClothModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_body', models.TextField()),
                ('star_given', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(limit_value=1), django.core.validators.MaxValueValidator(limit_value=5)])),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SummerClothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('isbn', models.PositiveIntegerField(unique=True)),
                ('image_cloth', models.ImageField(default=False, upload_to='media/summer_clothes_image/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('brand', models.CharField(blank=True, max_length=50, null=True)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'summerclothes_table',
            },
        ),
    ]
