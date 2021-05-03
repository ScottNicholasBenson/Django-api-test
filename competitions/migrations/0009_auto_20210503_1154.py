# Generated by Django 3.2 on 2021-05-03 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0008_alter_sellers_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='bids',
            name='seller',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='competitions.sellers'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='buyers',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='competitions',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitions.buyers'),
        ),
        migrations.AlterField(
            model_name='sellers',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
