# Generated by Django 4.0.4 on 2022-06-05 12:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispatcher', '0002_rename_date_act_date_created_act_date_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='act',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
    ]