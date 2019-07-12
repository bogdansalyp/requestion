# Generated by Django 2.2.1 on 2019-05-27 11:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0027_auto_20190527_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='creation_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 27, 11, 43, 51, 417084, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='answer',
            name='edit_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 27, 11, 43, 51, 417104, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='creation_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 27, 11, 43, 51, 415845, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='edit_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 27, 11, 43, 51, 415866, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 27, 11, 43, 51, 415408, tzinfo=utc)),
        ),
    ]