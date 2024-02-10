from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Assister)
admin.site.register(Administration)
admin.site.register(Etudiant)
admin.site.register(Encadrant)
admin.site.register(Note)
admin.site.register(Notification)
admin.site.register(Reunion)
admin.site.register(Stage)
