# Generated by Django 4.1.2 on 2022-12-12 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCamionetas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camionetas',
            name='foto',
            field=models.ImageField(upload_to='camionetas'),
        ),
    ]