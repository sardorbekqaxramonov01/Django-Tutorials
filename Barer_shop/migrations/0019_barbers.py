# Generated by Django 4.2.3 on 2023-07-28 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Barer_shop', '0018_service_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='media')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
