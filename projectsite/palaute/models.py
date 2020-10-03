import datetime
from django.db import models
from django.utils import timezone

# Testi models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)




# Palauteprojekti models
# Django luo id pääavaimen tauluille automaattisesti


class Kaupunki(models.Model):
    kaupunki_id = models.AutoField(primary_key=True)
    last_update = models.DateField(auto_now=False)
    kaupunki = models.CharField(max_length=30)
    def __str__(self):
        return self.kaupunki

class Osoite(models.Model):
    osoite_id = models.AutoField(primary_key=True)
    last_update = models.DateField(auto_now=False)
    kaupunki = models.CharField(max_length=30)
    osoite = models.CharField(max_length=30)
    postinumero = models.CharField(max_length=30)

    FK_kaupunki_id = models.ForeignKey(
        'Kaupunki',
        on_delete=models.RESTRICT
    )

class Toimipiste(models.Model):
    toimipiste_id = models.AutoField(primary_key=True)
    last_update = models.DateField(auto_now=False)
    '''One-to-one relationship'''
    FK_osoite_id = models.OneToOneField(
        'Osoite',
        on_delete=models.RESTRICT
    )
    toimipiste_nimi = models.CharField(max_length=30)


class Kayttajat(models.Model):
    '''Many-to-one relationship'''
    kayttaja_id = models.AutoField(primary_key=True)
    FK_osoite_id = models.ForeignKey(
        'Osoite',
        on_delete=models.RESTRICT
    )
    etunimi = models.CharField(max_length=30)
    sukunimi = models.CharField(max_length=30)
    kayttaja_nimi = models.CharField(max_length=30)
    salasana = models.CharField(max_length=30)
    sahkoposti = models.CharField(max_length=30)
    '''Automatically set the field to now every time the object is saved. 
    Useful for “last-modified” timestamps '''
    last_update = models.DateField(auto_now=False)


class Palaute(models.Model):
    palaute_id = models.AutoField(primary_key=True)
    '''Automatically set the field to now when the object is first created. 
    Useful for creation of timestamps'''
    palaute_pvm = models.DateField(auto_now=False)
    '''Many-to-one relationship'''
    FK_kayttaja_id = models.ForeignKey(
        'Kayttajat',
        on_delete=models.RESTRICT
    )
    '''Many-to-one relationship'''
    FK_toimipiste_id = models.ForeignKey(
        'Toimipiste',
        on_delete=models.RESTRICT
    )
    arvosana = models.PositiveIntegerField()
    hyvaa = models.TextField()
    huonoa = models.TextField()
    parannettavaa = models.TextField()


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
