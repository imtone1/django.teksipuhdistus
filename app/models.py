from django.db import models

class Teksti(models.Model):
    otsikko=models.CharField(max_length=100, default="")
    teksti=models.CharField(max_length=2000, default="")
    def __str__(self):
        return f"Otsikko: {self.otsikko} Teksti: {self.teksti}"

