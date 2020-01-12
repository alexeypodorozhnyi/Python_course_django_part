# Generated by Django 2.2 on 2020-01-11 21:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0007_auto_20191226_2135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_img', models.ImageField(null=True, upload_to='')),
                ('date_of_birth', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='name',
            field=models.CharField(default='My article', max_length=100),
        ),
        migrations.AlterField(
            model_name='article',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Profile'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='myapp.Article'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='myapp.Profile'),
        ),
        migrations.AlterField(
            model_name='like',
            name='article',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='myapp.Article'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.Profile'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]