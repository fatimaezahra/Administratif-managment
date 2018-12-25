# Generated by Django 2.1.3 on 2018-12-25 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0021_auto_20181225_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileinsurance',
            name='Patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='insurance.Person'),
        ),
    ]
