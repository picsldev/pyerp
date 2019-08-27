# Generated by Django 2.2.4 on 2019-08-27 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0067_pyproduct_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='PyCurrency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
                ('fc', models.DateTimeField(auto_now_add=True, null=True)),
                ('fm', models.DateTimeField(auto_now=True, null=True)),
                ('uc', models.IntegerField(blank=True, null=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=3, verbose_name='Nombre')),
                ('alias', models.CharField(max_length=40, verbose_name='Alias')),
                ('symbol', models.CharField(max_length=1, verbose_name='Símbolo')),
                ('position', models.CharField(choices=[('before', 'Antes de la Cantidad'), ('after', 'Después de la Cantidad')], default='after', max_length=64)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
