from django.shortcuts import render, redirect
from rest_framework import viewsets

from .models import *
from .serializers import *
# Create your views here.

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class AdministrateurViewSet(viewsets.ModelViewSet):
    queryset = Administrateur.objects.all()
    serializer_class = AdministrateurSerializer

class TechnicienViewSet(viewsets.ModelViewSet):
    queryset = Technicien.objects.all()
    serializer_class = TechnicienSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ProblemeViewSet(viewsets.ModelViewSet):
    queryset = Probleme.objects.all()
    serializer_class = ProblemeSerializer

class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer

class RelancerViewSet(viewsets.ModelViewSet):
    queryset = Relancer.objects.all()
    serializer_class = RelancerSerializer

def root(request):
    return redirect('api/')