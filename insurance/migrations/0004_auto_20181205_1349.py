# Generated by Django 2.1.2 on 2018-12-05 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0003_auto_20181205_1338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='fattening_date',
            new_name='hiring_date',
        ),
    ]
