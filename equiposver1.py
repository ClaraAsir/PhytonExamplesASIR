#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import os

def limpiar_pantalla():
    input("Pulsa INTRO para continuar...")
    os.system('clear')

dicequipos={}

masdatos='S'
#  Agregando datos al diccionarios de equipos
while masdatos!='N' and masdatos!='n':
    nombequipo=input("Indica el nombre del equipo: ")
    puntos=int(input("Indica los puntos del %s: " %nombequipo))
    dicequipos[nombequipo]=puntos
    masdatos=input("Quieres agregar un nuevo equipo (S/N): ")

limpiar_pantalla
# Recorriendo y mostrando datos del diccionarios de equipos
print("******** LISTADO DE EQUIPOS Y PUNTOS **************\n\n")
for equipo in dicequipos:
    print("%15s -> %3d" %(equipo,dicequipos[equipo]))