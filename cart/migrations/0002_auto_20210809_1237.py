# Generated by Django 2.2 on 2021-08-09 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210809_1149'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='items',
            new_name='item',
        ),
    ]
