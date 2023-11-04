# Generated by Django 4.2.2 on 2023-10-03 04:46

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.query
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('passdown', '0013_entry_cdi_entry_job_status_alter_entry_passdown_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='passdown',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='entry',
            name='passdown',
            field=models.ForeignKey(default=django.db.models.query.QuerySet.last, on_delete=django.db.models.deletion.CASCADE, to='passdown.passdown'),
        ),
    ]
