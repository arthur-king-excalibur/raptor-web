# Generated by Django 3.2.5 on 2022-08-26 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raptormc', '0019_alter_serverinformation_server_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='serverinformation',
            options={'verbose_name': 'Server Description', 'verbose_name_plural': 'Server Descriptions'},
        ),
    ]
