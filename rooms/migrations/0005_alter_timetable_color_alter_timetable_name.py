# Generated by Django 4.1.7 on 2023-11-03 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_timetable_color_timetable_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='color',
            field=models.CharField(default='White', max_length=50),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
