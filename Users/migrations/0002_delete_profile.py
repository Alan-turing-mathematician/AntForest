# Generated by Django 3.1 on 2020-10-10 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Forest', '0003_auto_20201010_1006'),
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]