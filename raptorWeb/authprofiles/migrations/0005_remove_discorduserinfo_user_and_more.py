# Generated by Django 4.1.5 on 2023-01-26 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authprofiles', '0004_remove_raptoruser_discord_user_info_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discorduserinfo',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='user',
        ),
        migrations.AddField(
            model_name='raptoruser',
            name='discord_user_info',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='authprofiles.discorduserinfo'),
        ),
        migrations.AddField(
            model_name='raptoruser',
            name='user_profile_info',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='authprofiles.userprofileinfo'),
        ),
    ]
