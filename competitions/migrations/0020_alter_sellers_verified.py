# Generated by Django 3.2 on 2021-05-03 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0019_auto_20210503_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellers',
            name='verified',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
