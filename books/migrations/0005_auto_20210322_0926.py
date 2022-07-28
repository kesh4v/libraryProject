# Generated by Django 3.1.6 on 2021-03-22 03:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20210322_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='dob',
            field=models.DateField(default=datetime.datetime(2021, 3, 22, 9, 26, 12, 472773)),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='image',
            field=models.ImageField(default='defaultuser.png', upload_to='users/image'),
        ),
    ]
