# Generated by Django 3.1.7 on 2021-05-11 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0017_auto_20210512_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_items_changelogs',
            name='adjust_detail',
            field=models.CharField(max_length=255),
        ),
    ]
