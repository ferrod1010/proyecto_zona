# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 02:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Repuesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=70)),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=30)),
                ('duenio', models.CharField(max_length=30)),
                ('anio', models.IntegerField()),
                ('repuestos', models.ManyToManyField(through='taller.Asignacion', to='taller.Repuesto')),
            ],
        ),
        migrations.AddField(
            model_name='asignacion',
            name='repuesto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taller.Repuesto'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='vehiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taller.Vehiculo'),
        ),
    ]
