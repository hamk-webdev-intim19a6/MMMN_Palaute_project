import datetime
from django.db import models
from django.utils import timezone
# Django luo id pääavaimen tauluille automaattisesti


class Osoite(models.Model):
    last_update = models.DateField(auto_now=False)
    kaupunki = models.CharField(max_length=30)
    osoite = models.CharField(max_length=30)
    postinumero = models.CharField(max_length=30)

    def __str__(self):
        return "%s, %s" % (self.osoite, self.kaupunki)


class Toimipiste(models.Model):
    last_update = models.DateField(auto_now_add=False)
    FK_osoite_id = models.OneToOneField(
        'Osoite',
        on_delete=models.RESTRICT
    )
    toimipiste_nimi = models.CharField(max_length=30)

    def __str__(self):
        return "%s, %s" % (self.toimipiste_nimi, self.FK_osoite_id.kaupunki)


class Palaute(models.Model):
    palaute_pvm = models.DateField(auto_now=False)
    '''Many-to-one relationship'''
    FK_toimipiste_id = models.ForeignKey(
        'Toimipiste',
        on_delete=models.RESTRICT
    )
    arvosana = models.PositiveIntegerField()
    hyvaa = models.TextField(blank=True)
    huonoa = models.TextField(blank=True)
    parannettavaa = models.TextField(blank=True)

    def __str__(self):
        return self.FK_toimipiste_id.toimipiste_nimi
