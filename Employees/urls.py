from django.urls import path
from Employees import views

app_name = 'Employees'

urlpatterns = [
    path('cv/<int:employee_id>/', views.employee_cv, name='employee_cv'),
    path('cv/<str:employee_position>/', views.cv_position, name='cv_position'),
    path('cv/', views.cv_general, name='cv_general'),]