from django.db import models
import uuid

# Create your models here.
class Utilisateur(models.Model):
    ROLE = (
        ('Admin', 'Admin'),
        ('Utilisateur', 'Utilisateur'),
        ('Technicien', 'Technicien'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=50, null=False)
    prenom = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False, unique=True)
    role = models.CharField(choices=ROLE, max_length=15, null=False)
    date_inscription= models.DateTimeField(auto_now_add=True, null=False)
    password = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.nom + " : " + self.role

class Service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=100, null=False)
    fonction = models.TextField(null=True)

    def __str__(self):
        return self.nom

class Client(Utilisateur):
    pass

class Administrateur(Utilisateur):
    pass

class Technicien(Utilisateur):
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)

class Probleme(models.Model):
    PRIORITY= (
        ('-1', 'Inconnu'),
        ('0', 'Normal'),
        ('1', 'Urgent'),
        ('2', 'Critique')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=50, null=False)
    description = models.TextField(null=True)
    priorite = models.IntegerField(choices=PRIORITY, default=-1)
    activate = models.BooleanField(default=False)

    def __str__(self):
        return self.nom


class Ticket(models.Model):
    STATE= (
        ('Non attribué', 'Non attribué'),
        ('En cours', 'En cours'),
        ('Terminé', 'Terminé')
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField(null=True)
    probleme = models.ForeignKey(Probleme, on_delete=models.SET_NULL, null=True)
    date_creation= models.DateTimeField(auto_now_add=True)
    etat = models.CharField(choices=STATE, max_length=20, null=False)
    service = models.ForeignKey(Service, on_delete=models.PROTECT, null=False)
    client = models.ForeignKey(Client, on_delete=models.PROTECT, null=False)
    technicien = models.ForeignKey(Technicien, on_delete=models.PROTECT, null=True)
    admin = models.ForeignKey(Administrateur, on_delete=models.PROTECT, null=True, related_name='admin')
    deleted = models.BooleanField(default=False)
    admin_deleted = models.ForeignKey(Administrateur, on_delete=models.SET_NULL, default=None, null=True, related_name='admin_deleted')

    def __str__(self):
        return str(self.id)

class Relancer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    ticket = models.ForeignKey(Ticket, on_delete=models.PROTECT, null=False)
    nombre_relance = models.IntegerField(default=1)

    def __str__(self):
        return str(self.date_created)

