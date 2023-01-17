# Generated by Django 3.2.5 on 2023-01-17 05:02

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_state', models.BooleanField(default=False)),
                ('in_maintenance', models.BooleanField(default=False, verbose_name='Maintenance Mode')),
                ('server_address', models.CharField(default='Default', max_length=50)),
                ('server_port', models.IntegerField(default=0)),
                ('modpack_name', models.CharField(default='Unnamed Modpack', max_length=100, verbose_name='Modpack Name')),
                ('modpack_version', models.CharField(default='1.0', max_length=100, verbose_name='Modpack Version')),
                ('modpack_description', ckeditor.fields.RichTextField(default='Modpack Description', max_length=1500, verbose_name='Modpack Description')),
                ('server_description', ckeditor.fields.RichTextField(default='Server Description', max_length=1500, verbose_name='Server Description')),
                ('server_rules', ckeditor.fields.RichTextField(default='Server-specific Rules', max_length=1500, verbose_name='Server-Specific Rules')),
                ('server_banned_items', ckeditor.fields.RichTextField(default='Server-specific Banned Items', max_length=1500, verbose_name='Server-specific Banned Items')),
                ('server_vote_links', ckeditor.fields.RichTextField(default='Server-specific Vote Links', max_length=1500, verbose_name='Voting Site Links')),
                ('modpack_picture', models.ImageField(blank=True, upload_to='modpack_pictures')),
                ('modpack_url', models.URLField(verbose_name='Link to Modpack')),
            ],
            options={
                'verbose_name': 'Server',
                'verbose_name_plural': 'Servers',
            },
        ),
        migrations.CreateModel(
            name='PlayerName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('server', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='gameservers.server')),
            ],
            options={
                'verbose_name': 'Player Name',
                'verbose_name_plural': 'Player Names',
            },
        ),
        migrations.CreateModel(
            name='PlayerCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_count', models.IntegerField(default=0)),
                ('server', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='gameservers.server')),
            ],
            options={
                'verbose_name': 'Player Count',
                'verbose_name_plural': 'Player Counts',
            },
        ),
    ]
