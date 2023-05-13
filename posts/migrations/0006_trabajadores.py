# Generated by Django 3.2.18 on 2023-04-29 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_productos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellidos', models.CharField(max_length=255)),
                ('rut', models.IntegerField()),
                ('fecha_nacimiento', models.CharField(max_length=255)),
                ('domicilio', models.CharField(max_length=255)),
                ('sexo', models.CharField(max_length=255)),
                ('nacionalidad', models.CharField(max_length=255)),
                ('tipo_contrato', models.CharField(max_length=255)),
                ('fecha_ingreso', models.CharField(max_length=255)),
            ],
        ),
    ]
