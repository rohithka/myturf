# Generated by Django 2.2.8 on 2022-11-16 05:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0018_auto_20221116_0931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createteammodel',
            name='tournament_id',
        ),
        migrations.AlterField(
            model_name='matchmodel',
            name='end_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 16, 10, 30, 57, 725266), max_length=30),
        ),
        migrations.AlterField(
            model_name='matchmodel',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 16, 10, 30, 57, 725244), max_length=30),
        ),
        migrations.AlterField(
            model_name='requestmodel',
            name='end_time',
            field=models.TimeField(blank=True, default='10:30:57'),
        ),
        migrations.AlterField(
            model_name='requestmodel',
            name='start_time',
            field=models.TimeField(blank=True, default='10:30:57'),
        ),
        migrations.AlterField(
            model_name='tournamentmodel',
            name='end_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 16, 10, 30, 57, 726283), max_length=30),
        ),
        migrations.AlterField(
            model_name='tournamentmodel',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 16, 10, 30, 57, 726269), max_length=30),
        ),
        migrations.AlterField(
            model_name='tournamentmodel',
            name='team_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='tournamentrequestmodel',
            name='end_time',
            field=models.TimeField(blank=True, default='10:30:57'),
        ),
        migrations.AlterField(
            model_name='tournamentrequestmodel',
            name='start_time',
            field=models.TimeField(blank=True, default='10:30:57'),
        ),
        migrations.AlterField(
            model_name='tournamentrequestmodel',
            name='team_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
