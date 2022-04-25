# Generated by Django 4.0.3 on 2022-04-24 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_principal', '0020_alter_port_type_port'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=158)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=158)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='switch',
            name='modele',
            field=models.CharField(max_length=50),
        ),
    ]
