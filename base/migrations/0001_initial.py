# Generated by Django 4.1.1 on 2022-10-29 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('active', models.BooleanField()),
                ('description', models.TextField(blank=True, null=True)),
                ('place', models.TextField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('ticked_side', models.IntegerField()),
                ('ticked_stand', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_active', models.DateTimeField()),
                ('date_deactive', models.DateTimeField()),
                ('date_from', models.DateTimeField()),
                ('date_to', models.DateTimeField()),
            ],
            options={
                'ordering': ['-date_created', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Type_event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', '-updated'],
            },
        ),
        migrations.AddField(
            model_name='event',
            name='type_event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.type_event'),
        ),
    ]
