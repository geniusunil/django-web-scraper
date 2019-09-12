# Generated by Django 2.2.4 on 2019-09-12 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainscrap', '0003_auto_20190911_1012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('csv_file', models.FileField(upload_to='documents/')),
            ],
        ),
        migrations.DeleteModel(
            name='csv_save',
        ),
    ]
