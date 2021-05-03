# Generated by Django 3.2 on 2021-05-03 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0002_auto_20210503_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='bids',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('created', models.DateTimeField()),
                ('accepted', models.BooleanField()),
                ('value', models.FloatField()),
                ('offered_capacity', models.IntegerField()),
                ('competition', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='competitions.competitions')),
            ],
        ),
        migrations.CreateModel(
            name='buyers',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='competitions.competitions')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='sellers',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='competitions.bids')),
                ('name', models.CharField(max_length=100)),
                ('verified', models.BooleanField()),
            ],
        ),
    ]