# Generated by Django 2.2 on 2020-01-28 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0007_shoppingevent_order_sum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reversalevent',
            name='shopping_event',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='market.ShoppingEvent'),
        ),
    ]