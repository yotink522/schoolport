# Generated by Django 3.1.7 on 2021-05-13 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0026_auto_20210514_0747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tb_course',
            name='course_color',
        ),
    ]