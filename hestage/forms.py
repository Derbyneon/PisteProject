from django import forms

class EtudiantForm(forms.Form):
    nom = forms.CharField(max_length=50)
    prenom = forms.CharField(max_length=100)
    date_naiss = forms.DateField()
    adresse_mail = forms.CharField(max_length=100)
    numtel = forms.IntegerField()
    nationalite = forms.CharField(max_length=30)
    cycle = forms.CharField(max_length=50)
    annee = forms.IntegerField()
    stage_trouve = forms.BooleanField()


class EncadrantForm(forms.Form):
    nom = forms.CharField(max_length=30)
    prenom = forms.CharField(max_length=50)
    adressemail = forms.CharField(max_length=70)
    matiere = forms.CharField(max_length=30)
    numtel = forms.IntegerField()
