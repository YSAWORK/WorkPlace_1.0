# Generated by Django 4.2.11 on 2025-01-30 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0008_employeesinfo_other_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attorneylicense',
            name='attorney_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Employees.employeesinfo'),
        ),
        migrations.AlterField(
            model_name='employeesinfo',
            name='other_info',
            field=models.TextField(blank=True, db_column='other_info', verbose_name='Додаткова інформація'),
        ),
    ]
