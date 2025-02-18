from django.shortcuts import render
from Clients.models import ClientsInfo, ClientActivities, ClientEmail, ClientPhone, ClientDates, ClientManagers

def clients_mainlist(request):
    clients = ClientsInfo.objects.all().order_by('client_name')
    return render(request, 'Clients/clients_general.html', context={'clients' : clients})

def client_cv(request, client_id: id):
    client = ClientsInfo.objects.get(pk=client_id)
    client_other_info = client.client_other_info.split('\n')
    activities = ClientActivities.objects.filter(client_id=client.pk).order_by('client_activities')
    emails = ClientEmail.objects.filter(client_id=client.pk).order_by('client_email')
    phones = ClientPhone.objects.filter(client_id=client.pk).order_by('phone')
    managers = ClientManagers.objects.filter(client_id=client.pk).order_by('client_manager_name')
    dates = ClientDates.objects.filter(client_id=client.pk).order_by('client_date__month', 'client_date__day', 'client_date__year')
    return render(request,'Clients/client_cv.html', {
        'client' : client,
        'client_other_info' : client_other_info,
        'activities' : activities,
        'managers' :  managers,
        'emails': emails,
        'dates' : dates,
        'phones' : phones})