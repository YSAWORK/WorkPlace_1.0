from django.forms import TextInput, Textarea
from django.db import models
from django.contrib import admin
from Clients.models import ClientsInfo, ClientActivities, ClientEmail, ClientPhone, ClientDates, ClientManagers, ClientAgreements, ClientAdditionalAgreements


@admin.register(ClientsInfo)
class ClientsInfoAdmin(admin.ModelAdmin):
# InLine підклас моделі ClientActivities
    class ActivitiesInLine(admin.TabularInline):
        model = ClientActivities
        extra = 0
# InLine підклас моделі ClientEmail
    class EmailInLine(admin.TabularInline):
        model = ClientEmail
        extra = 0
# InLine підклас моделі ClientPhone
    class PhoneInLine(admin.TabularInline):
        model = ClientPhone
        extra = 0
# InLine підклас моделі ClientDates
    class DateInLine(admin.TabularInline):
        model = ClientDates
        extra = 0
# InLine підклас моделі ClientManagers
    class ManagersInLine(admin.StackedInline):
        model = ClientManagers
        extra = 0
        formfield_overrides = {
            models.CharField: {'widget': TextInput(attrs={'size': '100'})},
            models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 100})}, }
# структура відображення моделі EmployeesInfo
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '100'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 10, 'cols': 100})},}
    fieldsets = (
        ("ОБОВ`ЯЗКОВА ІНФОРМАЦІЯ", {
            'classes': ['wide'],
            'fields': ('client_name', 'client_taxID', 'client_responsible_employee')
        }),
        (u'ДОДАТКОВА ІНФОРМАЦІЯ', {
            'classes': ['wide'],
            'fields': ('client_legal_address', 'client_postal_address', 'client_other_info', 'client_foto', ),
        }),)
    list_display = ['client_name', 'client_responsible_employee']
    inlines = [ActivitiesInLine, EmailInLine, PhoneInLine, ManagersInLine, DateInLine]


@admin.register(ClientAgreements)
class ClientAgreementsAdin(admin.ModelAdmin):
    # InLine підклас моделі ClientAdditionalAgreements
    class AdditionalAgreementsInLine(admin.StackedInline):
        model = ClientAdditionalAgreements
        extra = 0
    fields = ('client_id',
              'client_agreement_number',
              'client_agreement_date',
              'client_agreement_description',
              'client_agreement_representative_name',
              'client_agreement_representative_position',
              'client_agreement_file',)
    list_display = ['client_id',
                    'client_agreement_number',
                    'client_agreement_date',]
    list_filter = ["client_id"]
    inlines = [AdditionalAgreementsInLine,]
