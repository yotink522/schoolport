# Generated by Django 3.1.7 on 2021-05-10 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0014_auto_20210511_0204'),
    ]

    operations = [
        migrations.CreateModel(
            name='TB_Param_ParentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_type', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]