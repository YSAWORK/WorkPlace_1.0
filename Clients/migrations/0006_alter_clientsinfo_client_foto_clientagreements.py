# Generated by Django 4.2.11 on 2025-02-17 15:32

import Clients.models
import VBworkspace.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0005_clientmanagers_client_manager_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientsinfo',
            name='client_foto',
            field=models.ImageField(blank=True, db_column='client_foto', help_text='Завантажте фото клієнта (світлина, логотип, тощо)', null=True, upload_to=Clients.models.ClientsInfo.renamed_foto_location, verbose_name='фото клієнта'),
        ),
        migrations.CreateModel(
            name='ClientAgreements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_agreement_number', models.CharField(db_column='client_agreement_number', help_text='Введіть номер договору або б/н', max_length=50, unique=True, verbose_name='номер договору з клієнтом')),
                ('client_agreement_date', models.DateField(db_column='client_agreement_date', help_text='Оберіть дату укладення договору', validators=[VBworkspace.validators.validator_birth_date], verbose_name='дата укладення договору з клієнтом')),
                ('client_agreement_description', models.TextField(blank=True, db_column='client_agreement_description', max_length=500, verbose_name='Опис суті договору з клієнтом')),
                ('client_agreement_file', models.FileField(blank=True, db_column='client_agreement_file', upload_to=Clients.models.ClientAgreements.renamed_file_location, verbose_name='файл договору з клієнтом')),
                ('client_id', models.ForeignKey(db_column='client_id', on_delete=django.db.models.deletion.CASCADE, to='Clients.clientsinfo')),
            ],
            options={
                'verbose_name': 'Договір з клієнтом',
                'verbose_name_plural': 'Договори з клієнтом',
                'db_table': 'ClientAgreements',
            },
        ),
    ]
