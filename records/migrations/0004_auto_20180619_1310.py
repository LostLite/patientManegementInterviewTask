# Generated by Django 2.0.3 on 2018-06-19 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_auto_20180619_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='enrollment_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='enrollment_number',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
