from django.db import models


class przykladowa_osoba(models.Model):
    idOsoby = models.IntegerField()
    imieOsoby = models.CharField(max_length=240)

    def __str__(self):
        return 'Osoba: ' + self.nazwaFirmy

    class Meta:
        verbose_name_plural = "Obywatelki"