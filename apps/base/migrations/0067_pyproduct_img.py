# Generated by Django 2.2.4 on 2019-08-27 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0066_pyproductwebcategory_parent_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='pyproduct',
            name='img',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]
