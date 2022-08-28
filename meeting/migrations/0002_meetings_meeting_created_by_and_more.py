# Generated by Django 4.0 on 2022-08-28 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_groups_alter_user_user_permissions'),
        ('meeting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetings',
            name='meeting_created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
        migrations.AddField(
            model_name='meetings',
            name='meeting_timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]