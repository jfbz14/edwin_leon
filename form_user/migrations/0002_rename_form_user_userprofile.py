# Generated by Django 4.2 on 2023-04-18 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_user', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Form_user',
            new_name='UserProfile',
        ),
    ]
