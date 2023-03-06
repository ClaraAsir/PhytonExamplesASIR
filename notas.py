#! /usr/bin/env python
# -*- encoding: utf-8 -*-

try: 
	nota = int(input("Teclea la nota obtenida: "))

	if nota < 5:
		print ("%d es un suspenso" % nota)
	elif nota == 5:
		print ("%d es un suficiente" % nota)
	elif nota == 6:
		print ("%d es un bien" % nota)
	elif nota >= 7 and nota <= 8:
		print ("%d es un notable" % nota)
	elif nota >= 9 and nota <= 10:
		print ("%d es un sobre" % nota)
	else:
		print ("%d es una nota incorrecta" % nota)

except ValueError:
	print ("No es un valor correcto de nota")
