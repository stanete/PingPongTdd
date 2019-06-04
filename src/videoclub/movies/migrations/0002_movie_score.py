# Generated by Django 2.2.1 on 2019-06-04 12:48

from django.db import migrations, models
import rest_framework.compat


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='score',
            field=models.IntegerField(default=0, validators=[rest_framework.compat.MinValueValidator(0), rest_framework.compat.MaxValueValidator(10)]),
        ),
    ]
