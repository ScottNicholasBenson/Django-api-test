# Generated by Django 3.2 on 2021-05-03 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0004_alter_bids_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bids',
            name='competition',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='competitions',
            name='id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='competitions.bids'),
        ),
    ]
