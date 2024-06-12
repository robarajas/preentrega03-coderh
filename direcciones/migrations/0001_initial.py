# Generated by Django 5.0.6 on 2024-06-12 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=150)),
                ('ciudad', models.CharField(max_length=50)),
                ('codigo_postal', models.CharField(max_length=10)),
            ],
        ),
    ]
