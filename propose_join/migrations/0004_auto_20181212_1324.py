# Generated by Django 2.1.2 on 2018-12-12 07:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('propose_join', '0003_auto_20181121_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposedclub',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='proposedclub',
            name='pollend',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
