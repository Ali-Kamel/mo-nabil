# Generated by Django 2.0.3 on 2019-03-08 15:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aboutus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('Body1', models.TextField(default='')),
                ('Body2', models.TextField(default='')),
                ('Body3', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='contactinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(default='', max_length=100)),
                ('phone_number1', models.CharField(blank=True, default='', max_length=20)),
                ('phone_number2', models.CharField(blank=True, default='', max_length=20)),
                ('phone_number3', models.CharField(blank=True, default='', max_length=20)),
                ('phone_number4', models.CharField(blank=True, default='', max_length=20)),
                ('phone_number5', models.CharField(blank=True, default='', max_length=20)),
                ('phone_number6', models.CharField(blank=True, default='', max_length=20)),
                ('phone_number7', models.CharField(blank=True, default='', max_length=20)),
                ('phone_number8', models.CharField(blank=True, default='', max_length=20)),
                ('phone_number9', models.CharField(blank=True, default='', max_length=20)),
                ('phone_number10', models.CharField(blank=True, default='', max_length=20)),
                ('email1', models.EmailField(blank=True, default='youname@something.com', max_length=150)),
                ('email2', models.EmailField(blank=True, default='youname@something.com', max_length=150)),
                ('email3', models.EmailField(blank=True, default='youname@something.com', max_length=150)),
                ('email4', models.EmailField(blank=True, default='youname@something.com', max_length=150)),
                ('email5', models.EmailField(blank=True, default='youname@something.com', max_length=150)),
                ('email6', models.EmailField(blank=True, default='youname@something.com', max_length=150)),
                ('email7', models.EmailField(blank=True, default='youname@something.com', max_length=150)),
                ('email8', models.EmailField(blank=True, default='youname@something.com', max_length=150)),
                ('email9', models.EmailField(blank=True, default='youname@something.com', max_length=150)),
                ('email10', models.EmailField(blank=True, default='youname@something.com', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='homeproject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=500)),
                ('title2', models.CharField(blank=True, default='', max_length=500)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('text', models.CharField(default='', max_length=5000)),
                ('infowindow', models.TextField(default='')),
                ('img', models.ImageField(blank=True, upload_to='project/media/')),
            ],
        ),
    ]
