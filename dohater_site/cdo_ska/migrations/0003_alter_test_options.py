# Generated by Django 4.1.7 on 2023-03-11 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cdo_ska', '0002_alter_question_answer_alter_question_image_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='test',
            options={'ordering': ['-id']},
        ),
    ]
