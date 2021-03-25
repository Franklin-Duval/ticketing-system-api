from datetime import date
from django.shortcuts import render, redirect
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

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

    def create(self, request, *args, **kwargs):
        
        try:
            serializer = ClientSerializer(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()

            """ data = serializer.data[0]
            data.pop("date_inscription") """
            
            result = {
                "success": True,
                "message": "Client successfully created",
                "data": serializer.data
            }
            return Response(result, status=status.HTTP_201_CREATED)
        except:
            result = {
                "success": False,
                "message": "Client not created",
                "data": {}
            }
            return Response(result, status=status.HTTP_200_OK)


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


@api_view(['POST'])
def login(request):

    if (("email" not in request.data) or ("password" not in request.data)):
        result = {
            "success": False,
            "message": "Seul les champs 'email' et 'password' sont acceptés",
            "data": {}
        }
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
        
    if (request.method=='POST'):
        email = request.data["email"]
        password = request.data["password"]
        
        user = None
        try:
            user = Utilisateur.objects.filter(email=email, password=password)
            print(user, "\n")
            serializer = UtilisateurSerializer(user, many=True, context={'request': request})
            print(serializer.data)
            data = serializer.data[0]
            data.pop("date_inscription")
            result = {
                "success": True,
                "message": "La connexion s'est bien passée",
                "data": data
            }
            return Response(result, status=status.HTTP_200_OK)
        except:
            result = {
                "success": False,
                "message": "Vérifiez votre email et mot de passe",
                "data": {},
            }
            return Response(result)     

@api_view(['GET'])
def get_tickets(request):

    tickets = Ticket.objects.all()
    serializer = TicketSerializer(tickets, many=True, context={'request': request})

    serializer_ticket = serializer.data
    for ticket in serializer_ticket:
        #modify service field
        service = ticket["service"]
        id = service[service.find('service')+7: ]
        id = id.replace('/', '')

        service = Service.objects.get(id=id)
        serializer = ServiceSerializer(service, context={'request': request})
        ticket["service"] = serializer.data["nom"]
        
        #modify client field
        client = ticket["client"]
        id = client[client.find('client')+6: ]
        id = id.replace('/', '')

        client = Client.objects.get(id=id)
        serializer = ClientSerializer(client, context={'request': request})
        ticket["client"] = serializer.data["nom"] + " " + serializer.data["prenom"]

        #modify technician field
        tech = ticket["technicien"]
        if tech is None:
            ticket["technicien"] = "Aucun"
        else:
            id = tech[tech.find('technicien')+10: ]
            id = id.replace('/', '')

            tech = Technicien.objects.get(id=id)
            ticket["technicien"] = tech.nom + " " + tech.prenom

        #get priority of ticket
        problem = ticket["probleme"]

        if problem is None:
            ticket["priorite"] = "Inconnu"
        else:
            id = problem[problem.find('probleme')+8: ]
            id = id.replace('/', '')
            
            switcher = {
                -1: 'Inconnu',
                0: 'Normal',
                1: 'Urgent',
                2: 'Critique'
            }

            problem = Probleme.objects.get(id=id)
            ticket["priorite"] = switcher.get(problem.priorite, "Inconnu")
        
        ticket.pop('probleme')
        
        #arrange date format
        dates = ticket["date_creation"]
        dates = dates[ : 19]
        dates = dates.replace('T', ' à ')
        ticket["date_creation"] = dates
    
    result = {
        "success": True,
        "message": "Opération éffectuée avec succès",
        "data": serializer_ticket
    }

    return Response(result)

def root(request):
    return redirect('api/')