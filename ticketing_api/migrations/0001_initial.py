# Generated by Django 3.1.2 on 2021-03-23 08:25

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Probleme',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('priorite', models.IntegerField(default=-1)),
                ('activate', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('fonction', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.CharField(choices=[('Admin', 'Admin'), ('Utilisateur', 'Utilisateur'), ('Technicien', 'Technicien')], max_length=15)),
                ('date_inscription', models.DateTimeField(auto_now_add=True)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Administrateur',
            fields=[
                ('utilisateur_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ticketing_api.utilisateur')),
            ],
            bases=('ticketing_api.utilisateur',),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('utilisateur_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ticketing_api.utilisateur')),
            ],
            bases=('ticketing_api.utilisateur',),
        ),
        migrations.CreateModel(
            name='Technicien',
            fields=[
                ('utilisateur_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ticketing_api.utilisateur')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ticketing_api.service')),
            ],
            bases=('ticketing_api.utilisateur',),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.TextField(null=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('etat', models.CharField(choices=[('Non attribué', 'Non attribué'), ('En cours', 'En cours'), ('Terminé', 'Terminé')], max_length=20)),
                ('deleted', models.BooleanField(default=False)),
                ('probleme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ticketing_api.probleme')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketing_api.service')),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='admin', to='ticketing_api.administrateur')),
                ('admin_deleted', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='admin_deleted', to='ticketing_api.administrateur')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketing_api.client')),
                ('technicien', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ticketing_api.technicien')),
            ],
        ),
    ]
