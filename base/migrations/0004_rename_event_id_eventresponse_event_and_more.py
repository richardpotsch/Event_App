# Generated by Django 4.1.1 on 2022-10-30 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_event_price_eventresponse'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventresponse',
            old_name='event_id',
            new_name='event',
        ),
        migrations.RenameField(
            model_name='eventresponse',
            old_name='user_id',
            new_name='user',
        ),
    ]
