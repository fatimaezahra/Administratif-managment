# Generated by Django 2.1.3 on 2019-01-05 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0024_auto_20190105_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileinsurance',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.Status'),
        ),
    ]
