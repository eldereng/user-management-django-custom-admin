# Generated by Django 3.1.3 on 2020-12-13 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_professionalservices_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='checkin',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='people.checkin'),
        ),
    ]