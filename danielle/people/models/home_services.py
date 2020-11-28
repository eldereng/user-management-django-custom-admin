from django.db import models
from .base import BaseModel
from .person import Person


class HomeServices(BaseModel):
    class Meta:
        verbose_name_plural = "Serviços da casa"
        verbose_name = "Serviço da casa"

    person = models.ForeignKey(Person,
                               on_delete=models.PROTECT,
                               verbose_name="Pessoa")
    SERVICE_CHOICES = [('C', 'Café da manhã'), ('A', 'Almoço'), ('B', 'Banho'),
                       ('L', 'Lanche da tarde'), ('P', 'Per noite')]

    service = models.CharField(max_length=1,
                               verbose_name="Nome do serviço",
                               choices=SERVICE_CHOICES)

    def __str__(self):
        return self.person.name + " (" + self.service + ")"
