# Generated by Django 2.2.1 on 2019-05-26 15:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0008_auto_20190526_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='path',
            field=models.CharField(default='path', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='creation_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 26, 15, 25, 49, 108323, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='answer',
            name='edit_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 26, 15, 25, 49, 108351, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='creation_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 26, 15, 25, 49, 106756, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='edit_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 26, 15, 25, 49, 106782, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 26, 15, 25, 49, 106234, tzinfo=utc)),
        ),
    ]