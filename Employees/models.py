from django.db import models
from slugify import slugify
import Employees.validators, Employees.vocabularies, VBworkspace.validators

# МОДЕЛЬ: Досьє працівників
class EmployeesInfo(models.Model):
# Перейменування фото працівника в форматі slug та зазначення url для зберігання
    def renamed_foto_location(self, filename: str) -> str:
        filebase, extension = filename.split('.')
        filebase = slugify(f'{self.last_name} {self.first_name} {self.patronymic}')
        return 'Employees/images/personal_foto/%s.%s' % (filebase, extension)

# Налаштування формату окремих полів перед збереженням
    def save(self, *args, **kwargs):
        self.first_name = self.first_name.strip().capitalize()
        self.last_name = self.last_name.strip().capitalize()
        self.patronymic = self.patronymic.strip().capitalize()
        self.full_name = f'{self.last_name} {self.first_name} {self.patronymic}'
        return super(EmployeesInfo, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.full_name}'

# поля моделі
    last_name = models.CharField(
        blank=False,
        db_column='employee_last_name',
        help_text="Введіть прізвище працівника",
        null=False,
        max_length=200,
        validators=[Employees.validators.validator_name],
        verbose_name="прізвище",)
    first_name = models.CharField(
        blank=False,
        db_column='employee_first_name',
        help_text="Введіть ім'я працівника",
        null=False,
        max_length=200,
        validators=[Employees.validators.validator_name],
        verbose_name="ім'я",)
    patronymic = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="по-батькові",
        help_text="Введіть по-батькові працівника",
        validators=[Employees.validators.validator_name],
        db_column='employee_patronymic')
    full_name = models.CharField(
        max_length=500,
        null=False,
        blank=False,
        verbose_name="ПІБ",
        db_column='employee_full_name',
        editable=False,
        unique=True)
    gender = models.CharField(
        max_length=10,
        verbose_name="стать",
        help_text="Оберіть стать працівника",
        db_column='employee_gender',
        default='Не визначено',
        choices=Employees.vocabularies.Gender.choices)
    birth_date = models.DateField(
        blank=True,
        verbose_name="дата народження",
        help_text="Оберіть дату народження працівника",
        validators=[VBworkspace.validators.validator_birth_date],
        db_column='employee_birth_date')
    position=models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="посада",
        help_text="Оберіть посаду, на якій перебуває працівник",
        db_column='employee_position',
        choices=Employees.vocabularies.Position.choices)
    foto=models.ImageField(
        blank=False,
        db_column='employee_foto',
        help_text="Завантажте фото працівника",
        null=True,
        verbose_name="фото",
        upload_to=renamed_foto_location)
    other_info = models.TextField(
        blank=True,
        verbose_name='Додаткова інформація',
        db_column='other_info',
    )

    class Meta:
        ordering = ['full_name',]
        verbose_name = 'Досьє працівника'
        verbose_name_plural = 'Досьє працівників'
        db_table = 'EmployeeInfo'

# МОДЕЛЬ: база даних про Свідоцтва про зайняття адвокатською діяльністю (inLine з Employees.EmployeesInfo)
class AttorneyLicense(models.Model):
# Налаштування формату окремих полів перед збереженням
    def save(self, *args, **kwargs):
        self.serial = self.serial.strip().upper()
        self.number = self.number.strip()
        return super(AttorneyLicense, self).save(*args, **kwargs)

    def __str__(self):
        return f'Свідоцтво серії {self.serial} № {self.number}'

# Поля моделі
    attorney_name = models.OneToOneField(
        EmployeesInfo,
        on_delete=models.CASCADE)
    date_receipt = models.DateField(
        verbose_name="дата отримання Свідоцтва",
        help_text="Оберіть дату отримання Свідоцтва про право на зайняття адвокатською діяльністю",
        validators=[VBworkspace.validators.validator_birth_date],
        db_column='AttorneyLicense_date_receipt')
    authority = models.CharField(
        max_length=500,
        verbose_name="орган видачі",
        help_text="Оберіть орган адвокатського самоврядування, що видав Свідоцтво про право на зайняття адвокатською діяльністю",
        choices=Employees.vocabularies.LAWYER_MANAGEMENT_BODIES,
        db_column='AttorneyLicense_authority')
    serial = models.CharField(
        max_length=4,
        verbose_name="серія Свідоцтва",
        help_text="Введіть серію Свідоцтва про право на зайняття адвокатською діяльністю в форматі: АА",
        db_column='AttorneyLicense_serial',
        validators=[Employees.validators.validator_license_serial])
    number = models.CharField(
        max_length=10,
        verbose_name="№ Свідоцтва",
        help_text="Введіть № Свідоцтва про право на зайняття адвокатською діяльністю в форматі: 123456",
        db_column='AttorneyLicense_number',
        validators=[Employees.validators.validator_license_number])

    class Meta:
        verbose_name = 'Свідоцтво про право на зайняття адвокатською діяльністю'
        verbose_name_plural = 'Свідоцтва про право на зайняття адвокатською діяльністю'
        ordering = ['attorney_name', ]
        db_table = 'AttorneyLicense'

# МОДЕЛЬ: база даних про поштові адреси (inLine з Employees.EmployeesInfo)
class EmployeeEmail(models.Model):
    def __str__(self):
        return f'Електронні адреси працівника: {self.employee_name}'

    employee_name = models.ForeignKey(
        EmployeesInfo,
        on_delete=models.CASCADE,
        db_column='employee_name',)
    email = models.EmailField(
        blank=True,
        verbose_name='електронна пошта',
        help_text='Введіть робочу електронну пошту працівника',
        db_column='email',)

    class Meta:
        verbose_name = 'Електронна адреса'
        verbose_name_plural = 'Електронні адреси'
        db_table = 'EmployeeEmail'

# МОДЕЛЬ: база даних про номери телефонів (inLine з Employees.EmployeesInfo)
class EmployeePhone(models.Model):
    def __str__(self):
        return f'Телефонні номери працівника: {self.employee_name}'

    employee_name = models.ForeignKey(
        EmployeesInfo,
        on_delete=models.CASCADE,
        db_column='employee_name',)
    phone = models.CharField(
        max_length=13,
        blank=True,
        verbose_name='телефонний номер',
        help_text='Введіть телефонний номер працівника',
        validators= [VBworkspace.validators.validator_phone],
        db_column='phone_number',)

    class Meta:
        verbose_name = 'Телефонний номер'
        verbose_name_plural = 'Телефонні номери'
        db_table = 'EmployeePhone'

# МОДЕЛЬ: база даних про освіту (inLine з Employees.EmployeesInfo)
class EmployeeEducation(models.Model):
    def __str__(self):
        return f'Освіта працівника: {self.employee_name}'

    employee_name = models.ForeignKey(
        EmployeesInfo,
        on_delete=models.CASCADE,
        db_column = 'EmployeeEducation_employee_name',
        verbose_name = "ПІБ працівника",)
    university = models.CharField(
        max_length=300,
        verbose_name="Вищий навчальний заклад",
        help_text="Оберіть ВНЗ",
        choices=Employees.vocabularies.LEGAL_EDUCATION,
        db_column='EmployeeEducation_university')
    graduated_year = models.IntegerField(
        blank=True,
        verbose_name="Рік закінчення ВНЗ",
        help_text="Оберіть рік закінчення ВНЗ",
        choices=Employees.vocabularies.YEARS,
        db_column='EmployeeEducation_graduated_year')
    education_degree = models.CharField(
        max_length=20,
        verbose_name="Освітній/науковий ступінь",
        help_text="Оберіть освітній/науковий ступінь працівника",
        choices=Employees.vocabularies.EducationDegree.choices,
        db_column='EmployeeEducation_education_degree')

    class Meta:
        verbose_name = 'Освіта'
        verbose_name_plural = 'Освіта'
        ordering = ['employee_name', 'graduated_year', ]
        db_table = 'EmployeeEducation'

# МОДЕЛЬ: база даних нагород та відзнак (inLine з Employees.EmployeesInfo)
class EmployeeRewards(models.Model):
    def __str__(self):
        return f'Нагороди/відзнаки працівника: {self.employee_name}'

# поля моделі
    employee_name = models.ForeignKey(
        EmployeesInfo,
        on_delete=models.CASCADE,
        db_column='EmployeeRewards_employee_name',
        verbose_name="ПІБ працівника",)
    reward = models.CharField(
        max_length=500,
        verbose_name="нагорода/відзнака",
        help_text="Оберіть нагороду/відзнаку працівника",
        db_column='EmployeeRewards_reward')
    reward_auth = models.CharField(
        max_length=500,
        verbose_name="автор нагороди/відзнаки",
        help_text="Оберіть автора нагороди/відзнаки працівника",
        choices=Employees.vocabularies.RewardAuth.choices,
        db_column='EmployeeRewards_reward_auth')
    reward_year = models.IntegerField(
        verbose_name="рік отримання",
        help_text="Оберіть рік отримання відзнаки/нагороди",
        choices=Employees.vocabularies.YEARS,
        db_column='EmployeeRewards_reward_year')

    class Meta:
        verbose_name = 'Нагорода/відзнака'
        verbose_name_plural = 'Нагороди/відзнаки'
        ordering = ['employee_name', 'reward_year', ]
        db_table = 'EmployeeRewards'
