from django import views
from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import *

urlpatterns = [
    path('',home, name="home"),
    path('login',login, name="login"),
    path('register',register, name="register"),
    path('confirmation',confirmation, name="confirmation"),
    path('administrateur',administrateur, name="administrateur"),
    path('contact',contact, name="contact"),
    path('encadrant',encadrant, name="encadrant"),
    path('encadrant_form',encadrant_form, name="encadrant_form"),
    path('etudiant',etudiant, name="etudiant"),
    path('supprimer_etudiant/<int:id_etud>/', supprimer_etudiant, name='supprimer_etudiant'),
    path('etudiant_form',etudiant_form, name="etudiant_form"),
    path('propos',propos, name="propos"),
    path('reunion',reunion, name="reunion"),
    path('stage',stage, name="stage"),
    path('cv/<int:id_etud>/', cv_view, name='cv_view'),
    path('modifier_etudiant/<int:id_etud>/', modifier_etudiant, name='modifier_etudiant'),
    path('supprimer_stages',supprimer_stages, name='supprimer_stages'),
    path('administrateur_search',administrateur_search, name="administrateur_search"),
    path('encadrant_search',encadrant_search, name="encadrant_search"),
    path('etudiant_search',etudiant_search, name="etudiant_search"),
    path('reunion_search',reunion_search, name="reunion_search"),
    path('stage_search',stage_search, name="stage_search"),

]