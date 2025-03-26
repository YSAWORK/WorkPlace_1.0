from django.urls import path
from Clients import views

app_name = 'Clients'

urlpatterns = [
    path('', views.clients_mainlist, name='clients_mainlist'),
    path('cv/<int:client_id>/', views.client_cv, name='client_cv'),
    path('agreements/<int:agreement_id>/', views.client_agreement, name='client_agreement'),
    path('agreements/additional_agreements/<int:additional_agreement_id>/', views.client_additional_agreement, name='client_additional_agreement'),]