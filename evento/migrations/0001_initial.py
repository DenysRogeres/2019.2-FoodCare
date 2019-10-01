# Generated by Django 2.2.2 on 2019-10-01 23:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data_inicio', models.DateTimeField(default=datetime.datetime.now)),
                ('data_final', models.DateTimeField(default=datetime.datetime.now)),
                ('local', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Alimento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=60)),
                ('un_medida', models.CharField(max_length=60)),
                ('quantidade', models.IntegerField()),
                ('id_categoria', models.ManyToManyField(to='evento.Categoria')),
                ('id_evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evento.Evento')),
            ],
        ),
    ]
