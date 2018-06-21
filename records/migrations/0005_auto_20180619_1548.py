# Generated by Django 2.0.3 on 2018-06-19 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0004_auto_20180619_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='nok',
            field=models.ManyToManyField(blank=True, null=True, to='records.Patient'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_type',
            field=models.CharField(choices=[('T', 'Telephone'), ('E', 'Email'), ('A', 'Address')], max_length=15),
        ),
    ]