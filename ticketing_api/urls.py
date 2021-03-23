from django.urls import path, include
from rest_framework import routers

from . import views

routers = routers.DefaultRouter()
routers.register(r'administrateur', views.AdministrateurViewSet)
routers.register(r'ticket', views.TicketViewSet)
routers.register(r'technicien', views.TechnicienViewSet)
routers.register(r'client', views.ClientViewSet)
routers.register(r'service', views.ServiceViewSet)
routers.register(r'probleme', views.ProblemeViewSet)
routers.register(r'relance', views.RelancerViewSet)

urlpatterns = [
    path('', include(routers.urls)),
    path('login/', views.login)
]