from django.urls import path, include
from rest_framework import routers

from . import views

routers = routers.DefaultRouter()
routers.register(r'utilisateur', views.UtilisateurViewSet)
routers.register(r'administrateur', views.AdministrateurViewSet)
routers.register(r'ticket', views.TicketViewSet)
routers.register(r'technicien', views.TechnicienViewSet)
routers.register(r'client', views.ClientViewSet)
routers.register(r'service', views.ServiceViewSet)
routers.register(r'probleme', views.ProblemeViewSet)
routers.register(r'relance', views.RelancerViewSet)

urlpatterns = [
    path('', include(routers.urls)),
    path('login/', views.login),
    path('all-tickets/', views.get_tickets),
    path('new-tickets/', views.get_new_tickets),
    path('waiting-tickets/', views.get_waiting_tickets),
    path('finished-tickets/', views.get_finished_tickets),
    
    path('all-user-tickets/<str:id>/', views.get_user_tickets),
    path('waiting-user-tickets/<str:id>/', views.get_user_waiting_tickets),
    path('finished-user-tickets/<str:id>/', views.get_user_finished_tickets),

    path('all-technician-tickets/<str:id>/', views.get_technician_tickets),
    path('waiting-technician-tickets/<str:id>/', views.get_technician_waiting_tickets),
    path('finished-technician-tickets/<str:id>/', views.get_technician_finished_tickets),

    path('techniciens/', views.get_technicien),
]