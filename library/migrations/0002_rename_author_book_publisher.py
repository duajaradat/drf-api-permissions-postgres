# Generated by Django 3.2.9 on 2021-11-21 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='publisher',
        ),
    ]