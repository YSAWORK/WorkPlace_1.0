from django.core.exceptions import ValidationError
from datetime import date, timedelta

# Перевірка релевантності номеру телефону.
def validator_phone(value: str):
    if not value[1:].isdigit():
        raise ValidationError("Допустимі лише цифри після +")
    elif len(value) != 13:
        raise ValidationError("Потрібно ввести номер в форматі: +380501122233")
    elif value[0] != '+':
        raise ValidationError("Першим символом має бути +")

# Перевірка релевантності дати. Діапазон: від 100 років тому до сьогодні
def validator_birth_date(value: date):
    if value > date.today():
        raise ValidationError("Недопустима дата. Дата з майбутнього")
    elif value < (date.today() - timedelta(days=36000)):
        raise ValidationError("Недопустима дата. Люди стільки не живуть")