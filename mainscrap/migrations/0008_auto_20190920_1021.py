# Generated by Django 2.2.4 on 2019-09-20 04:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainscrap', '0007_auto_20190920_1010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='user',
        ),
        migrations.AddField(
            model_name='data',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
