# Generated by Django 3.2.9 on 2021-11-20 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0013_studentjournal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grade',
            old_name='profile_id',
            new_name='profile',
        ),
    ]
