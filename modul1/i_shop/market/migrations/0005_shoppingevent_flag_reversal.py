# Generated by Django 2.2 on 2020-01-26 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_auto_20200123_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingevent',
            name='flag_reversal',
            field=models.BooleanField(default=False),
        ),
    ]