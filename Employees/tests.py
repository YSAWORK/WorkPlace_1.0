from django.test import TestCase
from models import EmployeesInfo, EmployeeEducation

r = EmployeeEducation.objects.all()
r.get_employeesinfo_order()
print(r)