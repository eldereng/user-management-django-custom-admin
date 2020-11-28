from django.db import models
from .base import BaseModel
from .person import Person


class Checkin(BaseModel):
    class Meta:
        verbose_name_plural = "Check-in's"
        verbose_name = "Check-in"

    person = models.ForeignKey(Person,
                               verbose_name='Pessoa',
                               related_name='main_person',
                               on_delete=models.PROTECT)

    REASON_CHOICES = [('T', 'Paciente'), ('P', 'Acompanhante'),
                      ('F', 'Profissional'), ('V', 'Voluntário'),
                      ('S', 'Visitantes'), ('O', 'Outros')]

    reason = models.CharField(max_length=1,
                              choices=REASON_CHOICES,
                              verbose_name='Tipo de check-in')

    companion = models.ForeignKey(Person,
                                  blank=True,
                                  null=True,
                                  related_name='companion',
                                  verbose_name='Acompanhante',
                                  on_delete=models.PROTECT)

    TREATMENT_CHOICES = [('Q', 'Quimioterapia'), ('R', 'Radioterapia'),
                         ('S', 'Cirurgia'), ('E', 'Exames'), ('C', 'Consulta'),
                         ('O', 'Outro')]

    treatment = models.CharField(max_length=1,
                                 blank=True,
                                 null=True,
                                 choices=TREATMENT_CHOICES,
                                 verbose_name='Motivo')

    ca_number = models.CharField(max_length=20,
                                 blank=True,
                                 null=True,
                                 verbose_name='Número C.A.')

    social_vacancy = models.BooleanField(blank=True,
                                         null=True,
                                         verbose_name="Vaga Social?")

    observation = models.TextField(max_length=600,
                                   blank=True,
                                   null=True,
                                   verbose_name='Observação')

    def __str__(self):
        return self.person.name + " " + self.created_at.strftime(
            "(Entrada em %d/%m/%Y %H:%M)")
