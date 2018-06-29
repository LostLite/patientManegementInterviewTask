# Generated by Django 2.0.3 on 2018-06-28 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0009_patient_date_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditlog',
            name='action_type',
            field=models.CharField(choices=[('A', 'Add Record'), ('E', 'Edit Record'), ('D', 'Delete Record'), ('S', 'Search Operation')], max_length=1),
        ),
    ]
