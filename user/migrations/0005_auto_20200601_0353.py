# Generated by Django 3.0.6 on 2020-06-01 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_user_company'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='availavle',
            new_name='deleted',
        ),
    ]
