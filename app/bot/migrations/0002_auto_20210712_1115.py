# Generated by Django 3.2.4 on 2021-07-12 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metascompleted',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bot.profile'),
        ),
        migrations.AlterField(
            model_name='metasincomplete',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bot.profile'),
        ),
    ]
