# Generated by Django 4.2.11 on 2025-02-11 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientsinfo',
            options={'ordering': ['client_name'], 'verbose_name': 'Клієнт', 'verbose_name_plural': 'Клієнти'},
        ),
        migrations.AlterModelTable(
            name='clientsinfo',
            table='ClientsInfo',
        ),
    ]
