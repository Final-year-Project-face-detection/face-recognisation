# Generated by Django 3.1.1 on 2020-10-29 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentsAttendence', '0002_auto_20201029_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='cameranumbers',
            name='section',
            field=models.CharField(blank=True, choices=[('A', 'A Section'), ('B', 'B Section'), ('C', 'C Section')], max_length=1),
        ),
        migrations.AlterField(
            model_name='cameranumbers',
            name='year',
            field=models.CharField(blank=True, choices=[('1', 'First Year'), ('2', 'Second Year'), ('3', 'Third Year'), ('4', 'Fourth Year')], max_length=1),
        ),
    ]
