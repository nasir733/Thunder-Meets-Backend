# Generated by Django 4.0 on 2022-08-28 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0004_remove_meetings_agendas_agendas_meeting_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetings',
            name='meeting_date',
        ),
        migrations.RemoveField(
            model_name='meetings',
            name='meeting_time',
        ),
    ]
