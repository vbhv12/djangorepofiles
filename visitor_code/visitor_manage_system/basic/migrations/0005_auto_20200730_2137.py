# Generated by Django 3.0.8 on 2020-07-30 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0004_auto_20200730_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]