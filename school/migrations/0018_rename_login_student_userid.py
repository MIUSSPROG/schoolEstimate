# Generated by Django 3.2.9 on 2021-12-09 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0017_auto_20211209_0656'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='login',
            new_name='userId',
        ),
    ]