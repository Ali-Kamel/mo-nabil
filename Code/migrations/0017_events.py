# Generated by Django 2.0.3 on 2019-05-31 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Code', '0016_contactinfo_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=500)),
                ('text', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('img5', models.ImageField(blank=True, upload_to='Project')),
                ('img6', models.ImageField(blank=True, upload_to='Project')),
                ('img7', models.ImageField(blank=True, upload_to='Project')),
                ('img8', models.ImageField(blank=True, upload_to='Project')),
                ('img9', models.ImageField(blank=True, upload_to='Project')),
                ('title2', models.CharField(blank=True, default='', max_length=500)),
                ('text2', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('img1', models.ImageField(blank=True, upload_to='Project')),
                ('img2', models.ImageField(blank=True, upload_to='Project')),
                ('img3', models.ImageField(blank=True, upload_to='Project')),
                ('img4', models.ImageField(blank=True, upload_to='Project')),
            ],
        ),
    ]
