# Generated by Django 4.0.4 on 2022-06-02 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispatcher', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='act',
            old_name='date',
            new_name='date_created',
        ),
        migrations.AddField(
            model_name='act',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
