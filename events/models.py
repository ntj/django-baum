from django.db import models


class Person(models.Model):
    class Meta:
        verbose_name_plural = "Personen"
    vorname = models.CharField(max_length=200)
    nachname = models.CharField(max_length=200)


class Veranstaltung(models.Model):
    class Meta:
        verbose_name_plural = "Veranstaltungen"
    name = models.CharField(max_length=200)
    start = models.DateTimeField()
    end = models.DateTimeField()


class Person_Veranstaltung_Link(models.Model):
    person = models.ForeignKey('Person', on_delete=models.DO_NOTHING)
    veranstaltung = models.ForeignKey(
        'Veranstaltung', on_delete=models.DO_NOTHING)
