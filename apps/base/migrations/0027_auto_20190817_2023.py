# Generated by Django 2.2.4 on 2019-08-17 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0026_auto_20190817_2021'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pypartner',
            options={'ordering': ['-created_on']},
        ),
    ]