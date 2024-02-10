from django.db import models
from django.urls import reverse
from urllib.parse import urljoin


class Assister(models.Model):
    id_assister = models.AutoField(primary_key=True, verbose_name="ID")
    id_reunion = models.IntegerField(verbose_name="ID réunion")
    id_etud = models.IntegerField(verbose_name="ID étudiant")
    presence = models.BooleanField(verbose_name="Présence")

    class Meta:
        db_table = 'ASSISTER'
        verbose_name = "Assister"
        verbose_name_plural = "Assister"

    def __str__(self):
        return f"ID: {self.id_assister} | ID réunion: {self.id_reunion} | ID étudiant: {self.id_etud} | Présence: {self.presence}"


class Administration(models.Model):
    id_admin = models.AutoField(primary_key=True, verbose_name="id_admin")
    nom = models.CharField(max_length=30, verbose_name="Nom")
    prenom = models.CharField(max_length=50, verbose_name="Prénom")
    adressemail = models.CharField(max_length=70, verbose_name="Adresse e-mail")
    poste = models.CharField(max_length=30, verbose_name="Poste")
    numtel = models.IntegerField(verbose_name="Numéro de téléphone")

    class Meta:
        db_table = 'ADMINISTRATION'
        verbose_name = "Administration"
        verbose_name_plural = "Administrations"

    def __str__(self):
        return f"{self.nom} {self.prenom} ({self.poste})"

class Cv(models.Model):
    id_cv = models.AutoField(primary_key=True, blank=True, verbose_name="cv")
    pdf_file = models.FileField(upload_to='documents/')
class Etudiant(models.Model):
    id_etud = models.AutoField(primary_key=True, blank=True, verbose_name="id_etud")
    id_stage = models.IntegerField(blank=True, null=True, verbose_name="id_stage")
    id_note = models.IntegerField(blank=True, null=True, verbose_name="id_note")
    nom = models.CharField(max_length=50, blank=True, null=True, verbose_name="nom")
    prenom = models.CharField(max_length=100, blank=True, null=True, verbose_name="prenom")
    date_naiss = models.DateField(blank=True, null=True, verbose_name="date_naiss")
    adresse_mail = models.CharField(max_length=100, blank=True, null=True, verbose_name="adresse_mail")
    numtel = models.IntegerField(blank=True, null=True, verbose_name="numtel")
    nationalite = models.CharField(max_length=30, blank=True, null=True, verbose_name="nationalite")
    cycle = models.CharField(max_length=50, blank=True, null=True, verbose_name="cycle")
    cv = models.TextField(blank=True, null=True, verbose_name="cv")
    annee = models.IntegerField(blank=True, null=True, verbose_name="annee")
    stage_trouve = models.BooleanField(blank=True, null=True, verbose_name="stage_trouve")

    class Meta:
        db_table = 'ETUDIANT'
        verbose_name = "Etudiant"
        verbose_name_plural = "Etudiants"

    def __str__(self):
        return f"{self.nom} {self.prenom} ({self.cycle} - {self.annee})"
    def get_cv_url(self):
        if self.cv and hasattr(self.cv, 'name'):
            base_url = 'http://example.com/'  # Remplacez par l'URL de base de votre site
            cv_url = urljoin(base_url, self.cv.url)
            return cv_url
        else:
            return ''

class Encadrant(models.Model):
    id_encad = models.AutoField(primary_key=True, verbose_name="id_encad")
    nom = models.CharField(max_length=30, verbose_name="Nom")
    prenom = models.CharField(max_length=50, verbose_name="Prénom")
    adressemail = models.CharField(max_length=70, verbose_name="Adresse e-mail")
    matiere = models.CharField(max_length=30, verbose_name="Matière")
    numtel = models.IntegerField(verbose_name="Numéro de téléphone")

    class Meta:
        db_table = 'ENCADRANT'
        verbose_name = "Encadrant"
        verbose_name_plural = "Encadrants"

    def __str__(self):
        return f"{self.nom} {self.prenom} ({self.matiere})"


class Note(models.Model):
    id_note = models.AutoField(primary_key=True, verbose_name="id_note")
    id_encad = models.IntegerField(verbose_name="ID encadrant")
    id_etud = models.IntegerField(verbose_name="ID étudiant")
    note_cv = models.FloatField(verbose_name="Note CV")
    note_stage_trouve = models.FloatField(verbose_name="Note stage trouvé")
    note_sensibilisation = models.FloatField(verbose_name="Note sensibilisation")
    note_encadrant = models.FloatField(verbose_name="Note encadrant")
    note_total = models.FloatField(verbose_name="Note totale")

    class Meta:
        db_table = 'NOTE'
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self):
        return f"ID: {self.id_note} | ID encadrant: {self.id_encad} | ID étudiant: {self.id_etud} | Note totale: {self.note_total}"


class Notification(models.Model):
    id_notif = models.AutoField(primary_key=True, verbose_name="id_notif")
    id_admin = models.IntegerField(verbose_name="ID admin")
    adresse_envoi = models.CharField(max_length=70, verbose_name="Adresse d'envoi")
    adresse_reception = models.CharField(max_length=70, verbose_name="Adresse de réception")
    date_envoi = models.DateField(verbose_name="Date d'envoi")
    objet = models.CharField(max_length=200, verbose_name="Objet")
    fichier = models.CharField(max_length=70, verbose_name="Fichier")
    message = models.TextField(verbose_name="Message")

    class Meta:
        db_table = 'NOTIFICATION'
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"

    def __str__(self):
        return f"ID: {self.id_notif} | Objet: {self.objet} | Date d'envoi: {self.date_envoi}"


class Reunion(models.Model):
    id_reunion = models.AutoField(primary_key=True, verbose_name="id_reunion")
    nom_renuion = models.CharField(max_length=30, verbose_name="Nom de la réunion")
    date_debut = models.DateField(verbose_name="Date de début")
    annee = models.IntegerField(verbose_name="Année")
    filiere = models.CharField(max_length=100, verbose_name="Filière")

    class Meta:
        db_table = 'REUNION'
        verbose_name = "Réunion"
        verbose_name_plural = "Réunions"

    def __str__(self):
        return f"{self.nom_renuion} ({self.filiere})"


class Stage(models.Model):
    id_stage = models.AutoField(primary_key=True, verbose_name="id_stage")
    id_admin = models.IntegerField(verbose_name="ID admin")
    id_etud = models.IntegerField(verbose_name="ID étudiant")
    nom_stage = models.CharField(max_length=110, verbose_name="Nom du stage")
    type_stage = models.CharField(max_length=110, verbose_name="Type de stage")
    nom_entreprise = models.CharField(max_length=110, verbose_name="Nom de l'entreprise")
    email_entreprise = models.CharField(max_length=110, verbose_name="E-mail de l'entreprise")
    date_recherche = models.DateField(verbose_name="Date de recherche")
    date_debut = models.DateField(verbose_name="Date de début")
    date_fin = models.DateField(verbose_name="Date de fin")

    class Meta:
        db_table = 'STAGE'
        verbose_name = "Stage"
        verbose_name_plural = "Stages"

    def __str__(self):
        return f"ID: {self.id_stage} | Nom du stage: {self.nom_stage} | Nom de l'entreprise: {self.nom_entreprise}"


 