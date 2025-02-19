from django.core.validators import FileExtensionValidator
from django.db import models
from slugify import slugify
import VBworkspace.validators, Employees.models, Clients.vocabularies


class ClientsInfo(models.Model):
    # Перейменування фото клієнта в форматі slug та зазначення url для зберігання
    def renamed_foto_location(self, filename: str) -> str:
        filebase, extension = filename.split('.')
        filebase = slugify(f'{self.client_name}')
        return 'Clients/images/client_foto/%s.%s' % (filebase, extension)

    def __str__(self):
        return f'{self.client_name}'

    client_name = models.CharField(
        blank=False,
        db_column='client_name',
        help_text="Введіть ПІБ (для ФО) або найменування (для ЮО) клієнта",
        null=False,
        max_length=400,
        verbose_name="назва клієнта",)
    client_taxID = models.CharField(
        blank=True,
        db_column='client_taxID',
        help_text="Введіть РКНОПП (для ФО) або ЄДРПОУ (для ЮО) клієнта",
        max_length=15,
        verbose_name="реєстраційний номер клієнта клієнта",
        unique=True,)
    client_responsible_employee = models.ForeignKey(
        Employees.models.EmployeesInfo,
        on_delete=models.PROTECT,
        db_column='client_responsible_employee',
        verbose_name="відповідальний працівник",)
    client_legal_address = models.CharField(
        blank=False,
        db_column='client_legal_address',
        help_text="Введіть юридичну адресу клієнта (в форматі, що допустимий для процесуальних документів)",
        null=False,
        max_length=500,
        verbose_name="юридична адреса клієнта",)
    client_postal_address = models.CharField(
        blank=False,
        db_column='client_postal_address',
        help_text="Введіть поштову адресу клієнта (в форматі, що допустимий для процесуальних документів)",
        null=False,
        max_length=500,
        verbose_name="поштова адреса клієнта",)
    client_foto=models.ImageField(
        blank=True,
        db_column='client_foto',
        help_text="Завантажте фото клієнта (світлина, логотип, тощо)",
        null=True,
        verbose_name="фото клієнта",
        upload_to=renamed_foto_location)
    client_other_info = models.TextField(
        blank=True,
        db_column='client_other_info',
        verbose_name='Додаткова інформація про клієнта',)

    class Meta:
        ordering = ['client_name',]
        verbose_name = 'Клієнт'
        verbose_name_plural = 'Клієнти'
        db_table = 'ClientsInfo'


# Модель з базою даних бізнес-активностей клієнта
class ClientActivities(models.Model):
    def __str__(self):
        return f'Бізнес-активності клієнта: {self.client_id}'

    client_id = models.ForeignKey(
        ClientsInfo,
        db_column='client_id',
        on_delete=models.CASCADE,)
    client_activities = models.CharField(
        blank=False,
        choices=Clients.vocabularies.Client_activities_list.choices,
        db_column='client_activities',
        help_text="Оберіть бізнес активність клієнта",
        max_length=100,
        null=False,
        verbose_name="бізнес активність клієнта",)

    class Meta:
        verbose_name = 'Бізнес-активність клієнта'
        verbose_name_plural = 'Бізнес-активності Клієнта'
        db_table = 'ClientActivities'


# Модель з базою даних email клієнта
class ClientEmail(models.Model):
    def __str__(self):
        return f'Email клієнта: {self.client_id}'

    client_id = models.ForeignKey(
        ClientsInfo,
        db_column='client_id',
        on_delete=models.CASCADE,)
    client_email = models.CharField(
        blank=False,
        db_column='client_email',
        help_text="Введіть email клієнта",
        max_length=100,
        null=False,
        verbose_name="email клієнта",)

    class Meta:
        verbose_name = 'Email клієнта'
        verbose_name_plural = 'Перелік email Клієнта'
        db_table = 'ClientEmail'


# Модель з базою даних телефонних контактів клієнта
class ClientPhone(models.Model):
    def __str__(self):
        return f'Телефонні номери клієнта: {self.client_id}'

    client_id = models.ForeignKey(
        ClientsInfo,
        on_delete=models.CASCADE,
        db_column='client_id',)
    phone = models.CharField(
        blank=True,
        db_column='client_phone',
        help_text='Введіть телефонний номер клієнта',
        max_length=13,
        null=False,
        validators=[VBworkspace.validators.validator_phone],
        verbose_name='телефонний номер менеджера',)

    class Meta:
        verbose_name = 'Телефонний номер'
        verbose_name_plural = 'Телефонні номери'
        db_table = 'ClientPhone'


# Модель з базою даних важливих дат контактів клієнта
class ClientDates(models.Model):
    def __str__(self):
        return f'Ключові дати клієнта: {self.client_id}'

    client_id = models.ForeignKey(
        ClientsInfo,
        db_column='client_id',
        on_delete=models.CASCADE,)
    client_date = models.DateField(
        blank=False,
        db_column='client_date',
        help_text="Оберіть дату",
        null=False,
        validators=[VBworkspace.validators.validator_birth_date],
        verbose_name="важлива дата клієнта",)
    client_date_description = models.TextField(
        blank=False,
        db_column='client_date_description',
        max_length=500,
        verbose_name='Опис важливої дати клієнта',)

    class Meta:
        verbose_name = 'Важлива дата клієнта'
        verbose_name_plural = 'Важливі дати клієнта'
        db_table = 'ClientDates'


# Модель з базою даних менеджерів клієнта
class ClientManagers(models.Model):
    def __str__(self):
        return f'Менеджери клієнта: {self.client_id}'

    client_id = models.ForeignKey(
        ClientsInfo,
        db_column='client_id',
        on_delete=models.CASCADE,)
    client_manager_name = models.CharField(
        blank=False,
        db_column='client_manager_name',
        help_text="Введіть ПІБ менеджера клієнта",
        null=False,
        max_length=400,
        verbose_name="ПІБ менеджера клієнта",)
    client_manager_role = models.CharField(
        blank=False,
        db_column=' client_manager_role',
        help_text="Введіть статус/повноваження менеджера клієнта",
        null=False,
        max_length=400,
        verbose_name="статус/повноваження менеджера клієнта",)
    client_manager_email = models.CharField(
        blank=True,
        db_column='client_manager_email',
        help_text="Введіть email менеджера клієнта",
        max_length=100,
        null=False,
        verbose_name="email менеджера клієнта",)
    client_manager_phone = models.CharField(
        blank=True,
        db_column='client_manager_phone',
        help_text='Введіть телефонний номер менеджера клієнта',
        max_length=13,
        null=False,
        validators=[VBworkspace.validators.validator_phone],
        verbose_name='телефонний номер менеджера клієнта',)
    client_manager_other_info = models.TextField(
        blank=True,
        db_column='client_manager_other_info',
        verbose_name='Додаткова інформація про менеджера клієнта', )

    class Meta:
        verbose_name = f'Менеджер клієнта'
        verbose_name_plural = 'Менеджери клієнта'
        db_table = 'ClientManagers'


class ClientAgreements(models.Model):
    def __str__(self):
        return f''

    def renamed_file_location(self, filename: str) -> str:
        filebase, extension = filename.split('.')
        filebase = slugify(f'{ClientsInfo.objects.get(client_name=self.client_id).client_name}_{self.client_agreement_number}_{self.client_agreement_date}')
        return 'Clients/files/agreements/%s.%s' % (filebase, extension)

    client_id = models.ForeignKey(
        ClientsInfo,
        db_column='client_id',
        on_delete=models.CASCADE,)
    client_agreement_number = models.CharField(
        blank=False,
        db_column='client_agreement_number',
        help_text="Введіть номер договору або б/н",
        max_length=50,
        verbose_name="номер договору з клієнтом",
        unique=True)
    client_agreement_date = models.DateField(
        blank=False,
        db_column='client_agreement_date',
        help_text="Оберіть дату укладення договору",
        validators=[VBworkspace.validators.validator_birth_date],
        verbose_name="дата укладення договору з клієнтом",)
    client_agreement_description = models.TextField(
        blank=True,
        db_column='client_agreement_description',
        help_text="Додайте опис суті договору",
        max_length=500,
        verbose_name='Опис суті договору з клієнтом',)
    client_agreement_file = models.FileField(
        blank=True,
        db_column='client_agreement_file',
        help_text= "Додайте файл з договором в форматі PDF",
        validators= [FileExtensionValidator(allowed_extensions=['pdf'])],
        verbose_name='файл договору з клієнтом (pdf)',
        upload_to = renamed_file_location,)

    class Meta:
        verbose_name = f'Договір з клієнтом'
        verbose_name_plural = 'Договори з клієнтом'
        db_table = 'ClientAgreements'
