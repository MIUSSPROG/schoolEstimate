# Generated by Django 3.2.9 on 2021-11-20 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0009_auto_20211116_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
