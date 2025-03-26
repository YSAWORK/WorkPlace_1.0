from django.template.defaulttags import register
from django.shortcuts import render
from Clients.models import (ClientsInfo,
                            ClientActivities,
                            ClientEmail,
                            ClientPhone,
                            ClientDates,
                            ClientManagers,
                            ClientAgreements,
                            ClientAdditionalAgreements)


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
@register.filter
def get_list(dictionary, key):
    return [data.client_activities for data in dictionary.get(key)]

def clients_mainlist(request):
    clients = ClientsInfo.objects.all().order_by('client_name')
    agreements,activities = {}, {}
    for client in clients:
        agreements[client.pk] = ClientAgreements.objects.filter(client_id=client.pk)
    return render(request, 'Clients/1.2_clients_general.html', context={
        'clients' : clients,
        'agreements' : agreements})

def client_cv(request, client_id: id):
    client = ClientsInfo.objects.get(pk=client_id)
    activities = ClientActivities.objects.filter(client_id=client.pk).order_by('client_activities')
    agreements = ClientAgreements.objects.filter(client_id=client.pk).order_by('client_agreement_date')
    client_other_info = client.client_other_info.split('\n')
    dates = ClientDates.objects.filter(client_id=client.pk).order_by('client_date__month', 'client_date__day',                                                        'client_date__year')
    emails = ClientEmail.objects.filter(client_id=client.pk).order_by('client_email')
    managers = ClientManagers.objects.filter(client_id=client.pk).order_by('client_manager_name')
    phones = ClientPhone.objects.filter(client_id=client.pk).order_by('phone')
    return render(request,'Clients/1.1.1_client_cv.html', {
        'activities': activities,
        'agreements' : agreements,
        'client' : client,
        'client_other_info' : client_other_info,
        'dates': dates,
        'emails': emails,
        'managers' :  managers,
        'phones' : phones})

def client_agreement(request, agreement_id: id):
    agreement = ClientAgreements.objects.get(pk=agreement_id)
    agreement_description = agreement.client_agreement_description.split('\n')
    client = ClientsInfo.objects.get(pk=agreement.client_id.id)
    additional_agreements = ClientAdditionalAgreements.objects.filter(agreement_id=agreement.pk).order_by('client_additional_agreement_date')
    return render(request, 'Clients/1.1.2_client_agreement.html', {
        'agreement': agreement,
        'agreement_description' : agreement_description,
        'client': client,
        'additional_agreements' : additional_agreements})

def client_additional_agreement(request, additional_agreement_id: id):
    additional_agreement = ClientAdditionalAgreements.objects.get(pk=additional_agreement_id)
    additional_agreement_description = additional_agreement.client_additional_agreement_description.split('\n')
    client = ClientsInfo.objects.get(pk=additional_agreement.agreement_id.client_id.id)
    return render(request, 'Clients/1.1.3_client_additional_agreement.html', {
        'additional_agreement_description' : additional_agreement_description,
        'client': client,
        'additional_agreement' : additional_agreement})
