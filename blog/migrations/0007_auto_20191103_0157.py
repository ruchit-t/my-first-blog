# Generated by Django 2.2.6 on 2019-11-02 20:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20191103_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 2, 20, 27, 27, 325310, tzinfo=utc)),
        ),
    ]
