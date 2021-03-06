# Generated by Django 3.1.7 on 2021-05-09 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0007_tb_param_fees'),
    ]

    operations = [
        migrations.CreateModel(
            name='TB_Price_Standards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(null=True)),
                ('price_unit', models.CharField(max_length=50, null=True)),
                ('param_course_no', models.ForeignKey(db_column='param_course_no', on_delete=django.db.models.deletion.DO_NOTHING, related_name='f_course_no', to='app_core.tb_param_course')),
            ],
        ),
    ]
