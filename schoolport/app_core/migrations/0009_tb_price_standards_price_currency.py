# Generated by Django 3.1.7 on 2021-05-09 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0008_tb_price_standards'),
    ]

    operations = [
        migrations.AddField(
            model_name='tb_price_standards',
            name='price_currency',
            field=models.CharField(max_length=20, null=True),
        ),
    ]