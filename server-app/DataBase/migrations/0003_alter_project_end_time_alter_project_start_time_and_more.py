# Generated by Django 4.0.3 on 2022-03-11 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataBase', '0002_param_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='end_time',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_time',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login_time',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='regis_time',
            field=models.IntegerField(),
        ),
    ]
