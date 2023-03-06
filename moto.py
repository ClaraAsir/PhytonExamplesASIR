#! /usr/bin/env python
# -*- encoding: utf-8 -*-

from Vehiculo import *


class Moto(Vehiculo):
    """ Subclase Moto derivada de Vehículo """
    marcha = 0

    def __init__(self, litros, nmarcha):
        self.ruedas = 2
        self.marcha = nmarcha
        self.gasolina = litros

# Sobreescribe método arrancar()

    def arrancar(self):
        if self.gasolina > 0:
            print ("Moto arrancada")
        else:
            print ("Moto sin gasolina")

    def cambiarMarcha(self, camb_marcha):
        self.marcha = camb_marcha
        print ("Cambio de marcha")

mimoto = Moto(25, 2)
mimoto.arrancar()
print(mimoto.gasolina)
