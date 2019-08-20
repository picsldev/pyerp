# Generated by Django 2.2.4 on 2019-08-20 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0051_pyproduct_web_category_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='PyLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Nombre')),
                ('note', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
