# Generated by Django 4.1.7 on 2024-11-09 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='dob',
            field=models.DateField(default='2002-08-20'),
        ),
    ]