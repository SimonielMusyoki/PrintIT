# Generated by Django 2.2.2 on 2019-06-27 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printing', '0003_auto_20190627_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printitem',
            name='owner',
            field=models.CharField(default='', max_length=200),
        ),
    ]
