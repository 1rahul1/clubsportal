# Generated by Django 2.1.2 on 2018-12-12 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0018_auto_20181212_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='onpollclub',
            name='num_vote_down',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='onpollclub',
            name='num_vote_up',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='onpollclub',
            name='vote_score',
            field=models.IntegerField(db_index=True, default=0),
        ),
    ]
