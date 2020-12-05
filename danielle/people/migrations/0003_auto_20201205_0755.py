# Generated by Django 3.1.3 on 2020-12-05 10:55

from django.db import migrations, models
import utils.cep.check_cep
import utils.cpf.check_cpf
import utils.phone.check_phone


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20201205_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='cpf',
            field=models.CharField(blank=True, help_text='Exemplo: 00000000000', max_length=14, null=True, unique=True, validators=[utils.cpf.check_cpf.check_cpf], verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='person',
            name='message_phone',
            field=models.CharField(blank=True, help_text='Exemplo: 999999999', max_length=10, null=True, validators=[utils.phone.check_phone.check_phone], verbose_name='Tel. p/ mensagem'),
        ),
        migrations.AlterField(
            model_name='person',
            name='postal_code',
            field=models.CharField(blank=True, help_text='Exemplo: 00000000', max_length=15, null=True, validators=[utils.cep.check_cep.check_cep], verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='person',
            name='private_phone',
            field=models.CharField(blank=True, help_text='Exemplo: 999999999', max_length=10, null=True, validators=[utils.phone.check_phone.check_phone], verbose_name='Tel. p/ contato'),
        ),
    ]
