# Generated by Django 2.1.2 on 2018-12-06 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0004_auto_20181205_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relation',
            name='parental_relation',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
