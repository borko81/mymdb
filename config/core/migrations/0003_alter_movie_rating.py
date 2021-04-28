# Generated by Django 3.2 on 2021-04-28 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.IntegerField(choices=[(0, 'Not Rated'), (1, 'R - Restricted'), (2, 'G - General Audiences')]),
        ),
    ]