# Generated by Django 2.0.3 on 2019-03-09 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Code', '0003_cold_weld_facing_manufacture_piping_pressure_repair_spray_steel_tanks_welding'),
    ]

    operations = [
        migrations.AddField(
            model_name='cold_weld',
            name='title',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='facing',
            name='title',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='manufacture',
            name='title',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='piping',
            name='title',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='pressure',
            name='title',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='repair',
            name='title',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='spray',
            name='title',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='steel',
            name='title',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='tanks',
            name='title',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='welding',
            name='title',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='cold_weld',
            name='text',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='facing',
            name='text',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='manufacture',
            name='text',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='piping',
            name='text',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='pressure',
            name='text',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='repair',
            name='text',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='spray',
            name='text',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='steel',
            name='text',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='tanks',
            name='text',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='welding',
            name='text',
            field=models.CharField(default='', max_length=500, null=True),
        ),
    ]
