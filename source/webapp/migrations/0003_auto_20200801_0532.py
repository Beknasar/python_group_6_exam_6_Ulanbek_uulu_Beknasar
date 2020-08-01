# Generated by Django 2.2 on 2020-08-01 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20200731_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuestBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя автора записи')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('text', models.TextField(max_length=2000, verbose_name='Текст записи')),
                ('date_create', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_update', models.DateField(auto_now=True, verbose_name='Дата обновления')),
                ('status', models.CharField(choices=[('active', 'Активно'), ('blocked', 'Заблокировано')], default='active', max_length=25, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
