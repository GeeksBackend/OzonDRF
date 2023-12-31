# Generated by Django 4.2.6 on 2023-10-23 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название магазина')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание магазина')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='shop_logo/', verbose_name='Логотип')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Магазин',
                'verbose_name_plural': 'Магазины',
            },
        ),
    ]
