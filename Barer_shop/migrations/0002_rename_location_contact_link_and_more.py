# Generated by Django 4.2.3 on 2023-07-19 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Barer_shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='location',
            new_name='link',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='open_time',
        ),
    ]