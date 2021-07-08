# Generated by Django 3.2.4 on 2021-07-07 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MetasCompleted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255, unique=True)),
                ('metas', models.FloatField(blank=True, default=0)),
                ('metas_pro', models.FloatField(blank=True, default=0)),
                ('streak', models.BooleanField(blank=True)),
                ('streak_count', models.IntegerField(blank=True, default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MetasIncomplete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255, unique=True)),
                ('metas', models.FloatField(blank=True, default=0)),
                ('metas_pro', models.FloatField(blank=True, default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
