# Generated by Django 2.2 on 2021-08-10 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210809_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
