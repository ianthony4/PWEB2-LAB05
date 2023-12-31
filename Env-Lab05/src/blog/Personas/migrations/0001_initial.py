# Generated by Django 4.2.2 on 2023-06-14 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=100)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('genero', models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer'), ('ND', 'Prefiero no decirlo')], max_length=2)),
                ('ciudad', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
            ],
        ),
    ]
