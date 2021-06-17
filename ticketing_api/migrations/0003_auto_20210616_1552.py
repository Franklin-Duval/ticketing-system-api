# Generated by Django 3.1.2 on 2021-06-16 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing_api', '0002_auto_20210323_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='probleme',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='probleme',
            name='priorite',
            field=models.IntegerField(choices=[('-1', 'Inconnu'), ('0', 'Normal'), ('1', 'Urgent'), ('2', 'Critique')], default=-1),
        ),
    ]
