# Generated by Django 3.2.9 on 2021-11-06 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_auto_20211106_1645'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questionforgrade',
            options={'verbose_name': 'Вопрос для классы', 'verbose_name_plural': 'Вопросы для класса'},
        ),
    ]