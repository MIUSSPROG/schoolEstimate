# Generated by Django 3.2.9 on 2021-11-16 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0008_auto_20211106_1928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='theme',
            new_name='theme_id',
        ),
        migrations.AlterField(
            model_name='question',
            name='image_file',
            field=models.ImageField(default=None, upload_to='question_images/'),
        ),
    ]