# Generated by Django 3.1.3 on 2020-12-12 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='professionalservices',
            name='title',
            field=models.CharField(default='Sem título', max_length=120, verbose_name='Título'),
        ),
    ]
