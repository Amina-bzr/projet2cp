# Generated by Django 4.0.3 on 2022-04-11 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_principal', '0016_alter_vlan_num_vlan'),
    ]

    operations = [
        migrations.AddField(
            model_name='switch',
            name='password',
            field=models.CharField(default='pas de mot de passe', max_length=254, verbose_name='mot de passe'),
        ),
        migrations.AddField(
            model_name='switch',
            name='vlans',
            field=models.CharField(default='pas de VLANs associés', max_length=354),
        ),
    ]
