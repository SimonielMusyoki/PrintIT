# Generated by Django 2.2.2 on 2019-06-27 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('printing', '0002_auto_20190627_1037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='printitem',
            old_name='user',
            new_name='owner',
        ),
    ]