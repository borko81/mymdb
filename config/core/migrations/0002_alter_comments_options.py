# Generated by Django 3.2.5 on 2021-08-11 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['created_on']},
        ),
    ]
