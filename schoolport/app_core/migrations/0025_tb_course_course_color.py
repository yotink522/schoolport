# Generated by Django 3.1.7 on 2021-05-13 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0024_auto_20210513_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='tb_course',
            name='course_color',
            field=models.CharField(max_length=20, null=True),
        ),
    ]