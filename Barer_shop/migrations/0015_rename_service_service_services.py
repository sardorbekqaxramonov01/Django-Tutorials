# Generated by Django 4.2.3 on 2023-07-28 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Barer_shop', '0014_rename_services_service'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='Service',
            new_name='Services',
        ),
    ]
