# Generated by Django 2.1.3 on 2018-12-13 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0011_auto_20181213_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileinsurance',
            name='stat',
            field=models.CharField(blank=True, choices=[('Encours', 'encours'), ('Terminer', 'terminer')], max_length=20),
        ),
    ]