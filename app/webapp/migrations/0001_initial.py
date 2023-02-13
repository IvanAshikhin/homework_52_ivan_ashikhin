# Generated by Django 4.1.6 on 2023-02-13 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=500, verbose_name='Описание задачи')),
                ('status', models.CharField(default='new', max_length=100, verbose_name='Статус')),
                ('done_date', models.DateField(auto_now=True, verbose_name='Дата выполнения')),
            ],
        ),
    ]
