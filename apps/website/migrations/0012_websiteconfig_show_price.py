# Generated by Django 2.2.4 on 2019-08-29 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_websiteconfig_show_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='websiteconfig',
            name='show_price',
            field=models.BooleanField(default=True, verbose_name='Show price'),
        ),
    ]
