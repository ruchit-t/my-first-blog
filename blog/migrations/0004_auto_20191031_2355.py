# Generated by Django 2.2.6 on 2019-10-31 18:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191031_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 31, 18, 25, 4, 604296, tzinfo=utc)),
        ),
    ]
