from django.contrib import admin
from Employees.models import EmployeesInfo, AttorneyLicense, EmployeeEducation, EmployeeRewards, EmployeeEmail, EmployeePhone

@admin.register(EmployeesInfo)
class EmployeesInfoAdmin(admin.ModelAdmin):
# InLine підклас моделі AttorneyLicense
    class LicenseInLine(admin.StackedInline):
        model = AttorneyLicense
        extra = 0
        max_num = 1
# InLine підклас моделі EmployeeEducation
    class EducationInLine(admin.TabularInline):
        model = EmployeeEducation
        extra = 0
# InLine підклас моделі EmployeeRewards
    class RewardsInLine(admin.TabularInline):
        model = EmployeeRewards
        extra = 0
# InLine підклас моделі EmployeeEmail
    class EmailsInLine(admin.TabularInline):
        model = EmployeeEmail
        extra = 0
# InLine підклас моделі EmployeePhone
    class PhonesInLine(admin.TabularInline):
        model = EmployeePhone
        extra = 0


# структура відображення моделі EmployeesInfo
    fieldsets = [
        ('ОСОБИСТА ІНФОРМАЦІЯ', {"fields": ["last_name", 'first_name', 'patronymic', 'gender', 'birth_date', 'foto']}),
        ("РОБОЧА ІНФОРМАЦІЯ", {"fields": ["position", 'other_info'],}),]
    list_display = ['full_name', 'position']
    inlines = [EmailsInLine, PhonesInLine, EducationInLine, LicenseInLine, RewardsInLine]
