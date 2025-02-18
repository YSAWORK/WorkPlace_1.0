from django.shortcuts import render, get_object_or_404
from Employees.models import EmployeesInfo, EmployeeEducation, AttorneyLicense, EmployeeRewards, EmployeeEmail, EmployeePhone
from Clients.models import ClientsInfo
from Employees.vocabularies import Position


def employee_cv(request, employee_id: id):
    employee = get_object_or_404(EmployeesInfo, pk=employee_id)
    educations = EmployeeEducation.objects.filter(employee_name=employee.pk)
    try:
        attorney_license = AttorneyLicense.objects.get(attorney_name=employee_id)
    except AttorneyLicense.DoesNotExist:
        attorney_license = None
    rewards = EmployeeRewards.objects.filter(employee_name=employee.pk)
    emails = EmployeeEmail.objects.filter(employee_name=employee.pk)
    phones = EmployeePhone.objects.filter(employee_name=employee.pk)
    clients = ClientsInfo.objects.filter(client_responsible_employee=employee.pk)
    return render(request,'Employees/employee_cv.html', {
        'employee' : employee,
        'educations' : educations,
        "attorney_license" : attorney_license,
        'rewards' : rewards,
        'emails' : emails,
        'phones' : phones,
        'clients' : clients})

def cv_general(request):
    employees = EmployeesInfo.objects.all()
    positions = Position
    return render(request, 'Employees/cv_general.html', {
        'employees': employees,
        'positions' : positions})

def cv_position(request, employee_position):
    employees = EmployeesInfo.objects.filter(position=employee_position)
    return render(request, 'Employees/cv_position.html', {
        'employees': employees,
        'position': employee_position})