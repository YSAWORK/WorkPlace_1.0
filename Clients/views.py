from django.shortcuts import render
from Clients.models import ClientsInfo, ClientActivities, ClientEmail, ClientPhone, ClientDates, ClientManagers, ClientAgreements

def clients_mainlist(request):
    clients = ClientsInfo.objects.all().order_by('client_name')
    return render(request, 'Clients/clients_general.html', context={'clients' : clients})

def client_cv(request, client_id: id):
    client = ClientsInfo.objects.get(pk=client_id)
    activities = ClientActivities.objects.filter(client_id=client.pk).order_by('client_activities')
    agreements = ClientAgreements.objects.filter(client_id=client.pk).order_by('client_agreement_date')
    client_other_info = client.client_other_info.split('\n')
    dates = ClientDates.objects.filter(client_id=client.pk).order_by('client_date__month', 'client_date__day',                                                        'client_date__year')
    emails = ClientEmail.objects.filter(client_id=client.pk).order_by('client_email')
    managers = ClientManagers.objects.filter(client_id=client.pk).order_by('client_manager_name')
    phones = ClientPhone.objects.filter(client_id=client.pk).order_by('phone')
    return render(request,'Clients/client_cv.html', {
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
    return render(request, 'Clients/client_agreement.html', {
        'agreement': agreement,
        'agreement_description' : agreement_description,
        'client': client,})