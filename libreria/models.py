﻿# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django_enum import EnumField

TIPO_CLIENTE = (
    ('jurídico', 'Jurídico'),
    ('natural', 'Natural')
)

TIPO_EMPRESA = (
    ('turistica', 'Turistica'),
    ('oseo', 'Oseo'),
    ('educativa', 'Educativa'),
    ('salud', 'Salud')
)

TIPO_SALON = (
    ('convencional', 'Convencional'),
    ('bajo demanda', 'Bajo demanda')
)



class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'autor'


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    ciudad = models.CharField(max_length=30)
    codigo_postal = models.CharField(blank=True, null=True)
    tipo = models.CharField(
        max_length=100,
        choices=TIPO_CLIENTE
    )
    telefono = models.CharField(max_length=30, blank=True, null=True)
    nombre = models.CharField(max_length=70)
    id_empresa = models.ForeignKey('Empresa', on_delete=models.PROTECT, db_column='id_empresa', blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    fecha = models.DateField()
    id_empleado = models.ForeignKey('Empleado', on_delete=models.PROTECT, db_column='id_empleado')
    cantidad = models.IntegerField(blank=True, null=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, db_column='id_cliente', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compra'


class DetalleCompra(models.Model):
    libro = models.ForeignKey(
        'Libro',
        on_delete=models.CASCADE,
        db_column='isbn'
    )
    compra = models.ForeignKey(
        Compra,
        on_delete=models.CASCADE,
        db_column='id_compra'
    )

    class Meta:
        managed = False
        db_table = 'detalle_compra'
        unique_together = (('libro', 'compra'),)


class Editor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'editor'


class Editorial(models.Model):
    id_edit = models.AutoField(primary_key=True)
    telefono_conect = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    id_gerente = models.OneToOneField('Gerente', on_delete=models.PROTECT, db_column='id_gerente', blank=True, null=True,
                                      unique=True)
    pais = models.CharField(max_length=100, blank=True, null=True)
    isbn = models.OneToOneField('Libro', on_delete=models.PROTECT, db_column='isbn', blank=True, null=True,
                                unique=True)

    class Meta:
        managed = False
        db_table = 'editorial'


class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    born = models.DateField(blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)
    registro = models.DateField(blank=True, null=True, auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'empleado'


class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(
        max_length=100,
        choices=TIPO_EMPRESA
    )  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'empresa'


class Gerente(models.Model):
    id_gerente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'gerente'


class Libro(models.Model):
    isbn = models.CharField(primary_key=True, max_length=13)
    tema = models.CharField(max_length=30, blank=True, null=True)
    precio = models.FloatField()
    id_autor = models.ForeignKey(Autor, on_delete=models.PROTECT, db_column='id_autor', blank=True, null=True)
    id_editor = models.ForeignKey(Editor, on_delete=models.PROTECT, db_column='id_editor', blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'libro'


class Salon(models.Model):
    id_salon = models.AutoField(primary_key=True)
    editorial = models.ForeignKey(Editorial, models.DO_NOTHING, db_column='editorial', blank=True, null=True)
    capacidad = models.IntegerField(blank=True, null=True)
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado', blank=True, null=True)
    tipo = models.CharField(
        max_length=100,
        choices=TIPO_SALON
    )

    class Meta:
        managed = False
        db_table = 'salon'