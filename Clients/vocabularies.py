from django.db import models

class Client_activities_list(models.TextChoices):
    Banking = ('Банкінг', 'Банкінг')
    Gambling = ('Гемблінг', 'Гемблінг')
    Mining = ('Видобуток копалин', 'Видобуток копалин')
    Metallurgy = ('Металургія', 'Металургія')