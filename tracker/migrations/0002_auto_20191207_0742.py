# Generated by Django 3.0 on 2019-12-07 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mushi',
            old_name='date_created',
            new_name='date_posted',
        ),
    ]
