# Generated by Django 2.2 on 2019-12-23 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20191223_2028'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Likes',
            new_name='Like',
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]