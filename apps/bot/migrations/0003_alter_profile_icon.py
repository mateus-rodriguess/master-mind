# Generated by Django 3.2.4 on 2021-07-27 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_alter_leveluser_prestige_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='icon',
            field=models.CharField(blank=True, default='🙂', max_length=10, null=True),
        ),
    ]
