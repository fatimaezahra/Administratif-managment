# Generated by Django 2.0.1 on 2018-12-07 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0005_auto_20181206_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_image',
            field=models.ImageField(blank=True, null=True, upload_to='employee_image'),
        ),
    ]