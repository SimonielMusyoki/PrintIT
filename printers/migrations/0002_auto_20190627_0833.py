# Generated by Django 2.2.2 on 2019-06-27 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printer',
            name='closing_hours',
            field=models.TimeField(auto_now_add=True, help_text='The time your shop closes eg 5.00 p.m.'),
        ),
        migrations.AlterField(
            model_name='printer',
            name='opening_hours',
            field=models.TimeField(auto_now_add=True, help_text='The time your shop opens eg 8.00 a.m.'),
        ),
    ]
