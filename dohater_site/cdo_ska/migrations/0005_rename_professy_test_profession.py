# Generated by Django 4.1.7 on 2023-03-11 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cdo_ska', '0004_rename_professy_profession'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='professy',
            new_name='profession',
        ),
    ]