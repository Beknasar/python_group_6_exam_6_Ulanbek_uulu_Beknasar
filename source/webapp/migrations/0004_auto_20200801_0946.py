# Generated by Django 2.2 on 2020-08-01 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20200801_0532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestbook',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='guestbook',
            name='date_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
    ]