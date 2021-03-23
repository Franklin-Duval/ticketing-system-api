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
            user = Administrateur.objects.filter(email=email, password=password)
            serializer = AdministrateurSerializer(user, many=True, context={'request': request})
            
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



def root(request):
    return redirect('api/')