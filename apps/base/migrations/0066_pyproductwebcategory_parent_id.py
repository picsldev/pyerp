# Generated by Django 2.2.4 on 2019-08-24 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0065_pyproductcategory_parent_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='pyproductwebcategory',
            name='parent_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.PyProductWebCategory'),
        ),
    ]