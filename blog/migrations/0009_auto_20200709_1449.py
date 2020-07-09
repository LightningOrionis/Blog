# Generated by Django 3.0.8 on 2020-07-09 11:49

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200709_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.Blogger'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 9, 11, 49, 38, 641757, tzinfo=utc)),
        ),
    ]