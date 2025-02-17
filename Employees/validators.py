from django.core.exceptions import ValidationError


# Перевірка імен на наявність цифр, символів та пробілів
def validator_name(value: str):
    if not value.isalpha():
        raise ValidationError("Допустимі символи: А-Я, а-я, A-Z, a-z")


# Перевірка формату серії Свідоцтва адвоката (Employees.AttorneyLicense.serial)
def validator_license_serial(value: str):
    if not value.isalpha():
        raise ValidationError("Допустимі символи: А-Я")
    elif len(value) != 2:
        raise ValidationError("Потрібно 2 літери")

# Перевірка формату номера Свідоцтва адвоката (Employees.AttorneyLicense.number)
def validator_license_number(value: str):
    if not value.isdigit():
        raise ValidationError("Допустимі лише цифри")
    elif len(value) != 6:
        raise ValidationError("Потрібно 6 цифр")


