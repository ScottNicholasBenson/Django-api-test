# Generated by Django 3.2 on 2021-05-05 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0024_alter_closedcompetitiondata_associatedbuyer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='closedcompetitiondata',
            name='associatedBuyer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='competitions.buyers'),
        ),
    ]