# Generated by Django 3.2 on 2021-05-03 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0006_auto_20210503_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyers',
            name='id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='competitions.competitions'),
        ),
    ]
