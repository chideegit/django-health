# Generated by Django 5.0.6 on 2024-05-23 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='has_patient_profile',
            field=models.BooleanField(default=False),
        ),
    ]
