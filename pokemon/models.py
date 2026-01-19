from django.db import models

# Create your models here.

class Pokemon(models.Model):
    name = models.CharField(max_length=60)
    type1 = models.CharField(max_length=30)
    type2 = models.CharField(max_length=30, blank=True, null=True)
    level = models.PositiveIntegerField(default=1)
    hp = models.PositiveIntegerField(default=10)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.name}"
    

""" Cosa stai facendo qui:

    Stai definendo una tabella nel DB tramite una classe Python.

    Ogni Field (CharField, PositiveIntegerField, ecc.) diventa una colonna.

    Django aggiunge automaticamente un campo id (chiave primaria) → è quello che userai per la delete.
"""