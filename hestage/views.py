from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
import PyPDF2
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.conf import settings
from django.http import FileResponse, Http404
import os
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


# Create your views here.

def cv_view(request, id_etud):
    etudiant = get_object_or_404(Etudiant, id_etud=id_etud)
    cv = etudiant.cv
    if cv:
        response = HttpResponse(cv.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="{}"'.format(etudiant.cv.name)
        return response
    else:
        return HttpResponse("Aucun CV trouvé pour cet étudiant.")

    


def modifier_etudiant(request, id_etud):
    etudiant = get_object_or_404(Etudiant, id_etud=id_etud)
    if request.method == 'POST':
        etudiant.nom = request.POST['nom']
        etudiant.prenom = request.POST['prenom']
        etudiant.adresse_mail = request.POST['adresse_mail']
        etudiant.numtel = request.POST['numtel']
        etudiant.nationalite = request.POST['nationalite']
        etudiant.cycle = request.POST['cycle']
        etudiant.annee = request.POST['annee']
        etudiant.stage_trouve = 'stage_trouve' in request.POST
        etudiant.save()
        return redirect('confirmation')
    else:
        return render(request, 'modification_etudiant.html', {'etudiant': etudiant})
    

def supprimer_etudiant(request, id_etud):
    etudiant = get_object_or_404(Etudiant, id_etud=id_etud)
    if request.method == 'POST':
        etudiant.delete()
        return redirect('confirmation')
    else:
        return render(request, 'suppression_etudiant.html', {'etudiant': etudiant})




def contact(request):
    if request.method == 'POST':
        nom = request.POST.get('nom', '')
        email = request.POST.get('email', '')
        objet = request.POST.get('objet', '')
        message = request.POST.get('message', '')
        destinataire = 'jarvis1000@gmail.com'
        send_mail(
            objet,
            'De: ' + nom + ' (' + email + ')\n\n' + message,
            settings.EMAIL_HOST_USER,
            [destinataire],
            fail_silently=False,
        )
        return render(request, 'confirmation.html')
    else:
        return render(request, 'contact.html')


def confirmation(request):
    return render(request, 'confirmation.html')

def home(request):
    return render(request, ('home.html'))

def administrateur(request):
    administrations = Administration.objects.all()
    context = {'administrations': administrations}
    return render(request, 'administrateur.html', context)

def administrateur_search(request):
    query = request.GET.get('query')
    results = Administration.objects.filter(prenom__icontains=query)
    context = {'results': results}
    return render(request, 'administrateur_search.html', context)

def etudiant(request):
    etudiants = Etudiant.objects.all()
    context = {
        'etudiants': etudiants
    }
    return render(request, 'etudiant.html', context) 

def etudiant_form(request):
    if request.method == "POST":
        form = EtudiantForm(request.POST) 
        nom1 = request.POST.get("nom")
        prenom1 = request.POST.get("prenom")
        date_naiss1 = request.POST.get("date_naiss")
        adresse_mail1 = request.POST.get("adresse_mail")
        numtel1 = request.POST.get("numtel")
        nationalite1 = request.POST.get("nationalite")
        cycle1 = request.POST.get("cycle")
        annee1 = request.POST.get("annee")
        stage_trouve1 = request.POST.get("stage_trouve")
        Etudiant1 = Etudiant(
            nom=nom1,
            prenom=prenom1,
            date_naiss = date_naiss1,
            adresse_mail = adresse_mail1,
            numtel = numtel1,
            nationalite = nationalite1,
            cycle = cycle1,
            annee = annee1,
            stage_trouve = stage_trouve1
            
        )
        # Enregistrer l'objet Utilisateur dans la base de données
        Etudiant1.save()

        # Rediriger l'utilisateur vers une page de confirmation
        return redirect('confirmation')

    return render(request, 'register_etudiant.html')

def etudiant_search(request):
    query = request.GET.get('query')
    results = Etudiant.objects.filter(prenom__icontains=query)
    context = {'results': results}
    return render(request, 'etudiant_search.html', context)


def encadrant(request):
    encadrants = Encadrant.objects.all()
    context = {
        'encadrants': encadrants
    }
    return render(request, 'encadrant.html', context)

def encadrant_form(request):
    if request.method == "POST":
        nom1 = request.POST.get("nom")
        print(nom1)
        prenom1 = request.POST.get("prenom")
        adressemail1 = request.POST.get("adressemail")
        matiere1 = request.POST.get("matiere")
        numtel1 = request.POST.get("numtel")

        encadrant = Encadrant(
            nom = nom1,
        prenom = prenom1,
        adressemail = adressemail1,
        matiere = matiere1,
        numtel = numtel1,

        )
        # Enregistrer l'objet Utilisateur dans la base de données
        encadrant.save()

        # Rediriger l'utilisateur vers une page de confirmation
        return redirect('confirmation')

    return render(request, 'register_encadrant.html')

def encadrant_search(request):
    query = request.GET.get('query')
    results = Encadrant.objects.filter(prenom__icontains=query)
    context = {'results': results}
    return render(request, 'encadrant_search.html', context)

def reunion(request):
    reunions = Reunion.objects.all()
    context = {
        'reunions': reunions
    }
    return render(request, 'reunion.html', context)

def reunion_search(request):
    query = request.GET.get('query')
    results = Reunion.objects.filter(filiere__icontains=query)
    context = {'results': results}
    return render(request, 'reunion_search.html', context)

def stage(request):
    stages = Stage.objects.all()
    context = {
        'stages': stages
    }
    return render(request, 'stage.html', context)

def stage_search(request):
    query = request.GET.get('query')
    results = Stage.objects.filter(nom_stage__icontains=query)
    context = {'results': results}
    return render(request, 'stage_search.html', context)

def propos(request):
    return render(request, ('propos.html'))



def login(request):
    if request.method == "POST":
        prenom1 = request.POST.get('prenom')
        adressemail1 = request.POST.get('adressemail')

        # Vérifier si le prénom et l'adresse mail sont dans la table Administration
        admin = Administration.objects.filter(prenom=prenom1, adressemail=adressemail1).first()
        if admin:
            # Si un objet Administration est trouvé, l'utilisateur est valide
            return redirect('administrateur')
        else:
            # Sinon, l'utilisateur n'est pas valide et nous renvoyons un message d'erreur
            message = "Le prénom et/ou l'adresse mail ne sont pas valides."
            return render(request, 'login.html', {'message': message})
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        nom1 = request.POST.get('nom')
        prenom1 = request.POST.get('prenom')
        adressemail1 = request.POST.get('adressemail')
        poste1 = request.POST.get('poste')
        numtel1 = request.POST.get('numtel')
        # Créer un objet Utilisateur avec les données du formulaire
        administrateur = Administration(
            nom=nom1,
            prenom=prenom1,
            adressemail=adressemail1,
            poste=poste1,
            numtel=numtel1
        )
        # Enregistrer l'objet Utilisateur dans la base de données
        administrateur.save()

        # Rediriger l'utilisateur vers une page de confirmation
        return redirect('confirmation')

    return render(request, 'register.html')


def supprimer_stages(request):
    if request.method == 'POST':
        encadrants_selectionnes = request.POST.getlist('stages[]')
        for id_stage in encadrants_selectionnes:
            Stage.objects.filter(id_stage=id_stage).delete()
        return redirect('confirmation')
    else:
        return render(request, 'stage.html')



"""def view_pdf1(request, document_id):
    document1 = Cv.objects.get(id=id_cv)
    pdf_file = document1.pdf_file.path
    with open(pdf_file, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        page = pdf_reader.getPage(0)
        content = page.extractText()
    context = {
        'document1': document1,
        'content1': content1
    }
    return render(request, 'view_pdf1.html', context)

def view_pdf2(request, document_id):
    document2 = Cv.objects.get(id=id_cv)
    pdf_file = document2.pdf_file.path
    with open(pdf_file, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        page = pdf_reader.getPage(0)
        content2 = page.extractText()
    context = {
        'document2': document2,
        'content2': content2
    }
    return render(request, 'view_pdf2.html', context)
"""