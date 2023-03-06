#! /usr/bin/env python
# -*- encoding: utf-8 -*-


class Vehiculo:

    """ Abstracción de los objetos Vehiculo"""

    ruedas = 4
    gasolina = 0

    def __init__(self, litros, nruedas):
        self.gasolina = litros
        self.ruedas = nruedas
        print ("Tenemos ", litros, "litros")
        print ("Vehiculo de ", nruedas, "ruedas")

    def arrancar(self):
        if self.gasolina > 0:
            print ("Arranca")
        else:
            print ("Vehículo sin gasolina")

    def conducir(self):
        if self.gasolina > 0:
            self.gasolina -= 1
            print ("Quedan", self.gasolina, "litros")
        else:
            print ("No se mueve")
