# Generated by Django 2.2.1 on 2019-06-04 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Action'), (2, 'Comedy'), (3, 'Fantasy'), (4, 'Drama')], null=True),
        ),
    ]
