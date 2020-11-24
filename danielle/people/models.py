from django.db import models


class Person(models.Model):
    class Meta:
        verbose_name_plural = "Pessoas"
        verbose_name = "Pessoa"

    name = models.CharField(max_length=100, verbose_name='Nome')
    mother_name = models.CharField(max_length=100,
                                   blank=True,
                                   null=True,
                                   verbose_name='Nome da mãe')
    born_date = models.DateField(blank=True,
                                 null=True,
                                 verbose_name='Dt. nascimento')
    death_date = models.DateField(blank=True,
                                  null=True,
                                  verbose_name='Dt. óbito')
    email = models.EmailField(max_length=100,
                              blank=True,
                              null=True,
                              verbose_name='E-mail')
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]
    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES,
                              blank=True,
                              null=True,
                              verbose_name='Gênero')
    cpf = models.CharField(max_length=14,
                           blank=True,
                           null=True,
                           verbose_name='CPF')
    STATE_CHOICES = [("SP", "São Paulo"), ("PR", "Paraná"),
                     ("SC", "Santa Catarina"), ("RS", "Rio Grande do Sul"),
                     ("MS", "Mato Grosso do Sul"), ("RO", "Rondônia"),
                     ("AC", "Acre"), ("AM", "Amazonas"), ("RR", "Roraima"),
                     ("PA", "Pará"), ("AP", "Amapá"), ("TO", "Tocantins"),
                     ("MA", "Maranhão"), ("RN", "Rio Grande do Norte"),
                     ("PB", "Paraíba"), ("PE", "Pernambuco"),
                     ("AL", "Alagoas"), ("SE", "Sergipe"), ("BA", "Bahia"),
                     ("MG", "Minas Gerais"), ("RJ", "Rio de Janeiro"),
                     ("MT", "Mato Grosso"), ("GO", "Goiás"),
                     ("DF", "Distrito Federal"), ("PI", "Piauí"),
                     ("CE", "Ceará"), ("ES", "Espírito Santo")]
    rg = models.CharField(max_length=14,
                          blank=True,
                          null=True,
                          verbose_name='RG')
    rg_ssp = models.CharField(max_length=2,
                              choices=STATE_CHOICES,
                              blank=True,
                              null=True,
                              verbose_name='SSP')
    state = models.CharField(max_length=2,
                             choices=STATE_CHOICES,
                             blank=True,
                             null=True,
                             verbose_name='Estado')
    address_line_1 = models.CharField(max_length=100,
                                      blank=True,
                                      null=True,
                                      verbose_name='Endereço (linha 1)')
    address_line_2 = models.CharField(max_length=100,
                                      blank=True,
                                      null=True,
                                      verbose_name='Endereço (linha 2)')
    neighbourhood = models.CharField(max_length=60,
                                     blank=True,
                                     null=True,
                                     verbose_name='Bairro')
    city = models.CharField(max_length=60, blank=True, null=True)
    postal_code = models.CharField(max_length=15, blank=True, null=True)
    RESIDENCE_TYPE_CHOICES = [('U', 'Urbano'), ('R', 'Rural')]
    residence_type = models.CharField(max_length=1,
                                      choices=RESIDENCE_TYPE_CHOICES,
                                      blank=True,
                                      null=True,
                                      verbose_name='Distrito')
    private_phone = models.CharField(max_length=30,
                                     blank=True,
                                     null=True,
                                     verbose_name='Tel. p/ contato')
    message_phone = models.CharField(max_length=30,
                                     blank=True,
                                     null=True,
                                     verbose_name='Tel. p/ mensagem')
    observation = models.TextField(max_length=600,
                                   blank=True,
                                   null=True,
                                   verbose_name='Observação')
