# Generated by Django 3.1.3 on 2021-02-04 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_auto_20201213_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientCompanionCheckin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('companion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='companion_checkin', to='people.person', verbose_name='Acompanhante')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='patient_checkin', to='people.person', verbose_name='Paciente')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
