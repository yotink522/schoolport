# Generated by Django 3.1.7 on 2021-05-13 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0021_tb_fees'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tb_course',
            name='price_currency',
        ),
        migrations.RemoveField(
            model_name='tb_course',
            name='price_unit',
        ),
        migrations.AddField(
            model_name='tb_course',
            name='class_schedule_color',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tb_course',
            name='currency',
            field=models.CharField(default='CNY', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='tb_course',
            name='deduction_rule1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tb_course',
            name='deduction_rule2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tb_course',
            name='pricing_standard_nos',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tb_course',
            name='remarks',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='tb_course',
            name='type',
            field=models.IntegerField(default=1),
        ),
    ]
