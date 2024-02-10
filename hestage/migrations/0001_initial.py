# Generated by Django 4.2.2 on 2023-06-09 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administration',
            fields=[
                ('id_admin', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30, verbose_name='Nom')),
                ('prenom', models.CharField(max_length=50, verbose_name='Prénom')),
                ('adressemail', models.CharField(max_length=70, verbose_name='Adresse e-mail')),
                ('poste', models.CharField(max_length=30, verbose_name='Poste')),
                ('numtel', models.IntegerField(verbose_name='Numéro de téléphone')),
            ],
            options={
                'verbose_name': 'Administration',
                'verbose_name_plural': 'Administrations',
                'db_table': 'ADMINISTRATION',
            },
        ),
        migrations.CreateModel(
            name='Assister',
            fields=[
                ('id_assister', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('id_reunion', models.IntegerField(verbose_name='ID réunion')),
                ('id_etud', models.IntegerField(verbose_name='ID étudiant')),
                ('presence', models.BooleanField(verbose_name='Présence')),
            ],
            options={
                'verbose_name': 'Assister',
                'verbose_name_plural': 'Assister',
                'db_table': 'ASSISTER',
            },
        ),
        migrations.CreateModel(
            name='Encadrant',
            fields=[
                ('id_encad', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30, verbose_name='Nom')),
                ('prenom', models.CharField(max_length=50, verbose_name='Prénom')),
                ('adressemail', models.CharField(max_length=70, verbose_name='Adresse e-mail')),
                ('matiere', models.CharField(max_length=30, verbose_name='Matière')),
                ('numtel', models.IntegerField(verbose_name='Numéro de téléphone')),
            ],
            options={
                'verbose_name': 'Encadrant',
                'verbose_name_plural': 'Encadrants',
                'db_table': 'ENCADRANT',
            },
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_stage', models.IntegerField()),
                ('id_note', models.IntegerField()),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=100)),
                ('date_naiss', models.DateField()),
                ('adresse_mail', models.CharField(max_length=100)),
                ('numtel', models.IntegerField()),
                ('nationalite', models.CharField(max_length=30)),
                ('cycle', models.CharField(max_length=50)),
                ('cv', models.TextField()),
                ('annee', models.IntegerField()),
                ('stage_trouve', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Etudiant',
                'verbose_name_plural': 'Etudiants',
                'db_table': 'ETUDIANT',
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id_note', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('id_encad', models.IntegerField(verbose_name='ID encadrant')),
                ('id_etud', models.IntegerField(verbose_name='ID étudiant')),
                ('note_cv', models.FloatField(verbose_name='Note CV')),
                ('note_stage_trouve', models.FloatField(verbose_name='Note stage trouvé')),
                ('note_sensibilisation', models.FloatField(verbose_name='Note sensibilisation')),
                ('note_encadrant', models.FloatField(verbose_name='Note encadrant')),
                ('note_total', models.FloatField(verbose_name='Note totale')),
            ],
            options={
                'verbose_name': 'Note',
                'verbose_name_plural': 'Notes',
                'db_table': 'NOTE',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id_notif', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('id_admin', models.IntegerField(verbose_name='ID admin')),
                ('adresse_envoi', models.CharField(max_length=70, verbose_name="Adresse d'envoi")),
                ('adresse_reception', models.CharField(max_length=70, verbose_name='Adresse de réception')),
                ('date_envoi', models.DateField(verbose_name="Date d'envoi")),
                ('objet', models.CharField(max_length=200, verbose_name='Objet')),
                ('fichier', models.CharField(max_length=70, verbose_name='Fichier')),
                ('message', models.TextField(verbose_name='Message')),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
                'db_table': 'NOTIFICATION',
            },
        ),
        migrations.CreateModel(
            name='Reunion',
            fields=[
                ('id_reunion', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_renuion', models.CharField(max_length=30, verbose_name='Nom de la réunion')),
                ('date_debut', models.DateField(verbose_name='Date de début')),
                ('annee', models.IntegerField(verbose_name='Année')),
                ('filiere', models.CharField(max_length=100, verbose_name='Filière')),
            ],
            options={
                'verbose_name': 'Réunion',
                'verbose_name_plural': 'Réunions',
                'db_table': 'REUNION',
            },
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id_stage', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('id_admin', models.IntegerField(verbose_name='ID admin')),
                ('id_etud', models.IntegerField(verbose_name='ID étudiant')),
                ('nom_stage', models.CharField(max_length=110, verbose_name='Nom du stage')),
                ('type_stage', models.CharField(max_length=110, verbose_name='Type de stage')),
                ('nom_entreprise', models.CharField(max_length=110, verbose_name="Nom de l'entreprise")),
                ('email_entreprise', models.CharField(max_length=110, verbose_name="E-mail de l'entreprise")),
                ('date_recherche', models.DateField(verbose_name='Date de recherche')),
                ('date_debut', models.DateField(verbose_name='Date de début')),
                ('date_fin', models.DateField(verbose_name='Date de fin')),
            ],
            options={
                'verbose_name': 'Stage',
                'verbose_name_plural': 'Stages',
                'db_table': 'STAGE',
            },
        ),
    ]
