# Generated by Django 2.2.1 on 2019-05-26 15:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0013_auto_20190526_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='creation_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 26, 15, 58, 33, 131849, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='answer',
            name='edit_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 26, 15, 58, 33, 131881, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='creation_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 26, 15, 58, 33, 130148, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='edit_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 26, 15, 58, 33, 130178, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 26, 15, 58, 33, 129595, tzinfo=utc)),
        ),
    ]
