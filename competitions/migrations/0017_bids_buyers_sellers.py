# Generated by Django 3.2 on 2021-05-03 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0016_auto_20210503_1204'),
    ]

    operations = [
        migrations.CreateModel(
            name='buyers',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='sellers',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('verified', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='bids',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('created', models.DateTimeField()),
                ('accepted', models.BooleanField(blank=True, null=True)),
                ('value', models.FloatField()),
                ('offered_capacity', models.IntegerField()),
                ('competition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='competitions.competitions')),
                ('seller', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='competitions.sellers')),
            ],
        ),
    ]
