# Generated by Django 2.1.3 on 2018-12-03 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0003_auto_20181202_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileinsurance',
            name='amount_rreimbursement',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='fileinsurance',
            name='amount',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='fileinsurance',
            name='file_number',
            field=models.IntegerField(null=True),
        ),
    ]