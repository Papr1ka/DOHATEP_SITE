# Generated by Django 4.1.7 on 2023-03-08 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cdo_ska', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='professy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdo_ska.professy'),
        ),
    ]