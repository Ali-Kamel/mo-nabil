# Generated by Django 2.0.3 on 2019-04-30 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Code', '0011_auto_20190430_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fubrication_errection_of_steel_structure',
            name='img1',
            field=models.ImageField(upload_to='Project'),
        ),
        migrations.AlterField(
            model_name='fubrication_errection_of_steel_structure',
            name='img2',
            field=models.ImageField(upload_to='Project'),
        ),
        migrations.AlterField(
            model_name='fubrication_errection_of_steel_structure',
            name='img3',
            field=models.ImageField(upload_to='Project'),
        ),
        migrations.AlterField(
            model_name='fubrication_errection_of_steel_structure',
            name='img4',
            field=models.ImageField(upload_to='Project'),
        ),
    ]
