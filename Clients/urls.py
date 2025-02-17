from django.urls import path
from Clients import views

app_name = 'Clients'

urlpatterns = [
    path('', views.clients_mainlist, name='clients_mainlist'),
    path('cv/<int:client_id>/', views.client_cv, name='client_cv'),]