from django.db import models


class Modelo(models.Model):
    nome = models.CharField(max_length=80)

    def __str__(self):
        return self.nome