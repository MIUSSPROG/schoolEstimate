# Generated by Django 3.2.9 on 2021-12-10 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0018_rename_login_student_userid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='theme_id',
            new_name='theme',
        ),
    ]