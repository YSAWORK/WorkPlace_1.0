# Generated by Django 4.2.11 on 2025-02-19 10:10

import Clients.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0007_alter_clientagreements_client_agreement_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientagreements',
            name='client_agreement_file',
            field=models.FileField(blank=True, db_column='client_agreement_file', default='Clients/files/agreements/default.pdf', help_text='Додайте файл з договором в форматі PDF', upload_to=Clients.models.ClientAgreements.renamed_file_location, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='файл договору з клієнтом (pdf)'),
        ),
    ]
