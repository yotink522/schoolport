# Generated by Django 3.1.7 on 2021-05-11 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0019_auto_20210512_0442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_items_changelogs',
            name='adjust_detail',
            field=models.CharField(max_length=512),
        ),
    ]