# Generated by Django 5.0.1 on 2024-02-03 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summer_clothes', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summerclothes',
            name='image_cloth',
            field=models.ImageField(default=False, upload_to='media/summer_clothes_image'),
        ),
    ]