# Generated by Django 3.2.18 on 2023-04-29 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20230429_0454'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=255)),
                ('valor', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('categoria', models.CharField(max_length=255)),
            ],
        ),
    ]
