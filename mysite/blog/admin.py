from django.contrib import admin
from .models import Voetbalspeler

@admin.register(Voetbalspeler)
class VoetbalspelerAdmin(admin.ModelAdmin):
    list_display = ("naam", "actuele_voetbalclub", "auteur", "datum_invoer", "laatste_aanpassing")
    search_fields = ("naam", "actuele_voetbalclub")