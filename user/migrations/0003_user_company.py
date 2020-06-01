# Generated by Django 3.0.6 on 2020-05-29 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20200528_0732'),
        ('user', '0002_auto_20200528_0732'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Company'),
        ),
    ]
