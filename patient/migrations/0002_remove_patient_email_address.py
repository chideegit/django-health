# Generated by Django 5.0.6 on 2024-05-23 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='email_address',
        ),
    ]
