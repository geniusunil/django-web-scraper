# Generated by Django 2.2.4 on 2019-09-11 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainscrap', '0002_auto_20190911_0955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csv_save',
            name='csv_file',
        ),
        migrations.RemoveField(
            model_name='csv_save',
            name='url',
        ),
        migrations.RemoveField(
            model_name='csv_save',
            name='username',
        ),
        migrations.AddField(
            model_name='csv_save',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='csv_save',
            name='price',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
