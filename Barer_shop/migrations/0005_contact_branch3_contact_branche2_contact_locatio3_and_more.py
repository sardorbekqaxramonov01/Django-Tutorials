# Generated by Django 4.2.3 on 2023-07-21 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Barer_shop', '0004_contact_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='branch3',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='branche2',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='locatio3',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='location2',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
