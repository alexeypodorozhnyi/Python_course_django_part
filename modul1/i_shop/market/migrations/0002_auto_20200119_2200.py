# Generated by Django 2.2 on 2020-01-19 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingevent',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='authorisation.Profile'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
