# Generated by Django 4.0.3 on 2022-05-21 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_principal', '0040_historique'),
    ]

    operations = [
        migrations.AlterField(
            model_name='port',
            name='type_suiv',
            field=models.CharField(choices=[('Prise', 'Prise'), ('Switch', 'Switch'), ("Point d'accés", "Point d'accés"), ('Imprimante', 'Imprimante'), ('Aucun', 'Aucun'), ('Autre', 'Autre')], default='Aucun', max_length=15, verbose_name="Type de l'appareil relié "),
        ),
    ]