# Generated by Django 2.2.4 on 2019-08-20 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20190819_2249'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_blog', models.BooleanField(default=False, verbose_name='Mostrar Blog')),
                ('show_shop', models.BooleanField(default=False, verbose_name='Mostrar Tienda')),
            ],
        ),
    ]