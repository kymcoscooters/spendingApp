# Generated by Django 3.1.3 on 2020-12-27 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spending', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nameStyle',
            field=models.CharField(default='', max_length=200),
        ),
    ]
