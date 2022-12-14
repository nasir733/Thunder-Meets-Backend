# Generated by Django 4.0 on 2022-08-28 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0003_agendas_meetings_agendas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetings',
            name='agendas',
        ),
        migrations.AddField(
            model_name='agendas',
            name='meeting',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agendas', to='meeting.meetings'),
        ),
        migrations.AlterField(
            model_name='agendas',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='agendas',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
