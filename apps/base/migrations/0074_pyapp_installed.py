# Generated by Django 2.2.4 on 2019-08-31 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0073_pyapp'),
    ]

    operations = [
        migrations.AddField(
            model_name='pyapp',
            name='installed',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]