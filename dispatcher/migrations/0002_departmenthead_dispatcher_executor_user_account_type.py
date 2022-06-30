# Generated by Django 4.0.4 on 2022-06-29 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispatcher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentHead',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('dispatcher.account',),
        ),
        migrations.CreateModel(
            name='Dispatcher',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('dispatcher.account',),
        ),
        migrations.CreateModel(
            name='Executor',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('dispatcher.account',),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('dispatcher.account',),
        ),
        migrations.AddField(
            model_name='account',
            name='type',
            field=models.CharField(choices=[('USER', 'User'), ('DISPATCHER', 'Dispatcher'), ('DEPARTMENT_HEAD', 'Department_head'), ('EXECUTOR', 'Executor')], default='USER', max_length=50, verbose_name='Type'),
        ),
    ]