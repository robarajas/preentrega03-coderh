# Generated by Django 5.0.6 on 2024-07-04 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosextra',
            name='rol_usuario',
            field=models.CharField(choices=[('C', 'Comprador'), ('V', 'Vendedor')], default='C', max_length=1),
        ),
        migrations.AlterField(
            model_name='datosextra',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], default='O', max_length=1),
        ),
    ]