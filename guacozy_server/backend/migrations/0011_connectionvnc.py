# Generated by Django 2.2.6 on 2019-10-21 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_connection_name_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConnectionVnc',
            fields=[
                ('connection_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='backend.Connection')),
                ('autoretry', models.IntegerField(default=10)),
                ('color_depth', models.CharField(choices=[('8', '8 bits'), ('16', '16 bits'), ('24', '24 bits'), ('32', '32 bits')], default='8', max_length=2)),
                ('swap_red_blue', models.BooleanField(default=False)),
                ('cursor_remote', models.BooleanField(default=False)),
                ('read_only', models.BooleanField(default=False)),
                ('repeater_dest_host', models.CharField(blank=True, max_length=60)),
                ('repeater_dest_port', models.IntegerField(default=0)),
                ('reverse_connect', models.BooleanField(default=False)),
                ('listen_timeout', models.IntegerField(default=5)),
                ('clipboard_encoding', models.CharField(choices=[('ISO8859-1', 'ISO8859-1'), ('UTF-8', 'UTF-8'), ('UTF-16', 'UTF-16'), ('CP1252', 'CP1252')], default='ISO8859-1', max_length=16)),
            ],
            options={
                'verbose_name': 'VNC Connection',
                'verbose_name_plural': 'VNC Connections',
            },
            bases=('backend.connection',),
        ),
    ]