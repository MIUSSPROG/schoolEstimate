# Generated by Django 3.2.9 on 2021-11-20 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0015_auto_20211120_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentjournal',
            name='answer',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='studentjournal',
            name='correct',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='studentjournal',
            name='score',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
