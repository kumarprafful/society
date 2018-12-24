# Generated by Django 2.1.4 on 2018-12-24 19:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('starting_share', models.IntegerField()),
                ('starting_loan', models.IntegerField()),
                ('date_of_creation', models.DateTimeField(default=datetime.datetime.now)),
                ('month_of_creation', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MonthlyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('month', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('previous_loan', models.IntegerField()),
                ('share', models.IntegerField()),
                ('total_share', models.IntegerField()),
                ('installment', models.IntegerField()),
                ('balance_loan', models.IntegerField()),
                ('interest', models.IntegerField()),
                ('late_fees', models.IntegerField(default=0)),
                ('total_amount', models.IntegerField()),
                ('remarks', models.CharField(blank=True, max_length=30, null=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='record.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Society',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('society_name', models.CharField(max_length=1024, unique=True)),
                ('president', models.CharField(max_length=1024)),
                ('address', models.CharField(max_length=1024)),
                ('date_of_creation', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'Society',
                'verbose_name_plural': 'Societies',
            },
        ),
        migrations.AddField(
            model_name='member',
            name='society',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='record.Society'),
        ),
    ]
