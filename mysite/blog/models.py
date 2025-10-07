from django.conf import settings
from django.db import models
from django.utils import timezone


class Voetbalspeler(models.Model):
    naam = models.CharField(max_length=100)
    actuele_voetbalclub = models.CharField(max_length=100)
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    datum_invoer = models.DateTimeField(default=timezone.now)
    laatste_aanpassing = models.DateTimeField(auto_now=True)

    def publiceer(self):
        """Slaat de invoer op en stelt laatste aanpassing bij."""
        self.laatste_aanpassing = timezone.now()
        self.save()

    def __str__(self):
        return self.naam