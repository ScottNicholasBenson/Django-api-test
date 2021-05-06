# Generated by Django 3.2 on 2021-05-05 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0022_closedcompetitiondata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='closedcompetitiondata',
            name='associatedBuyer',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='closedcompetitiondata',
            name='offeredCapacity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='closedcompetitiondata',
            name='percentageAcceptedBids',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='closedcompetitiondata',
            name='totalValueAcceptedBids',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
