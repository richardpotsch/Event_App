# Generated by Django 4.1.1 on 2022-10-30 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_rename_event_id_eventresponse_event_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date_active',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_deactive',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_to',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='ticked_side',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='ticked_stand',
            field=models.IntegerField(blank=True),
        ),
    ]
