# Generated by Django 4.0.4 on 2022-07-03 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0009_alter_cars_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/cars'),
        ),
    ]