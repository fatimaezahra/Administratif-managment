# Generated by Django 2.1.3 on 2018-12-20 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0017_fileinsurance_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('in_progres', 'In progress'), ('finished', 'Finished'), ('refused', 'Refused')], default='in_progres', max_length=220)),
            ],
        ),
        migrations.AlterField(
            model_name='fileinsurance',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='insurance.Status'),
        ),
    ]
