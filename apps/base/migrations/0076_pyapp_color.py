# Generated by Django 2.2.4 on 2019-08-31 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0075_auto_20190831_0403'),
    ]

    operations = [
        migrations.AddField(
            model_name='pyapp',
            name='color',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Color'),
        ),
    ]
