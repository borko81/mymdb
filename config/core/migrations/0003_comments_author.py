# Generated by Django 3.2.3 on 2021-07-18 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210718_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='author',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
