# Generated by Django 3.1.7 on 2021-06-22 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPeludo', '0002_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascotas',
            name='codigo',
            field=models.CharField(max_length=6),
        ),
    ]