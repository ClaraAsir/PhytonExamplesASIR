# Función CalcularFactorial: recibe un número entero y
# devuelve su factorial.
# Deberá tratar las excepciones.
# Parámetros de entrada: numero (int)
# Valores de salida: factorial (int)

#! /usr/bin/env python
# -*- encoding: utf-8 -*-

try:
	def CalculaFactorial(numero):
		if numero == 0:
			factorial = 1
		else:
			factorial = numero
			while numero > 1:
				numero-=1
				factorial=factorial*numero
		return factorial


	num=int(input("Teclea el número: "))
	print("El factorial de %d es: %d" % (num,CalculaFactorial(num)))

except ValueError:
	print("Debes teclear un número entero")

