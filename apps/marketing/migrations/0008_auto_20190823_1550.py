# Generated by Django 2.2.4 on 2019-08-23 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0007_auto_20190823_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pycampaign',
            name='uc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pychannel',
            name='uc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pymform',
            name='uc',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
