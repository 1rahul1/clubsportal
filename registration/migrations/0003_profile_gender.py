# Generated by Django 2.1.2 on 2018-11-11 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20181111_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('M', 'male'), ('F', 'Female'), ('N', 'None')], default='N', max_length=1),
        ),
    ]
