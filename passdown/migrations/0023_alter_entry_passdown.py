# Generated by Django 4.2.2 on 2023-10-11 18:11

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.query


class Migration(migrations.Migration):

    dependencies = [
        ('passdown', '0022_remove_workcenter_organization_alter_entry_passdown_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='passdown',
            field=models.ForeignKey(default=django.db.models.query.QuerySet.last, on_delete=django.db.models.deletion.CASCADE, to='passdown.passdown'),
        ),
    ]
