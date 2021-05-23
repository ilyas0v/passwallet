# Generated by Django 3.2.3 on 2021-05-23 08:14

import django_cryptography.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credential', '0003_auto_20210523_0813'),
    ]

    operations = [
        migrations.AddField(
            model_name='credential',
            name='email_name',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=100)),
        ),
        migrations.AddField(
            model_name='credential',
            name='email_password',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=200)),
        ),
        migrations.AddField(
            model_name='credential',
            name='email_username',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=100)),
        ),
    ]