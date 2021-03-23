# Generated by Django 3.1.2 on 2021-03-23 09:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='probleme',
            name='priorite',
            field=models.IntegerField(choices=[('-1', 'Inconnu'), ('0', 'Normal'), ('1', 'Urgent'), ('2', 'Très urgent'), ('3', 'Critique')], default=-1),
        ),
        migrations.CreateModel(
            name='Relancer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('nombre_relance', models.IntegerField(default=1)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketing_api.ticket')),
            ],
        ),
    ]
