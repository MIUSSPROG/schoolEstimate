# Generated by Django 3.2.9 on 2021-11-20 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0011_rename_profile_grade_profile_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionforgrade',
            name='score',
        ),
    ]