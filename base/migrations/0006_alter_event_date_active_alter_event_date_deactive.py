# Generated by Django 4.1.1 on 2022-11-05 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_event_date_active_alter_event_date_deactive_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date_active',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_deactive',
            field=models.DateField(blank=True),
        ),
    ]
