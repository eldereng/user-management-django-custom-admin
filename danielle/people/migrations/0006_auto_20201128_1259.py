# Generated by Django 3.1.3 on 2020-11-28 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_professionalservices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='reason',
            field=models.CharField(choices=[('T', 'Paciente'), ('P', 'Acompanhante'), ('F', 'Profissional'), ('V', 'Voluntário'), ('S', 'Serviços'), ('O', 'Outros')], max_length=1, verbose_name='Tipo de check-in'),
        ),
    ]
