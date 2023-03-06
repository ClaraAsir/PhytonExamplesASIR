#! /usr/bin/env python
# -*- encoding: utf-8 -*-

contador=1
listaalumnos=[]
listanotas=[]
notasalumnos=[]
cont=0
tuplanotas=('ISO','FH','LM','REDES')

while contador < 6:
	nombrealumno=input("Introduce el nombre del alumno: ")
	listaalumnos.append(nombrealumno)
	contador+=1
	
for alumno in listaalumnos:
	while cont < len(tuplanotas):
		nota=input("Alumno %15s. Nota de %14s: " %(alumno,tuplanotas[cont]))
		cont+=1
		listanotas.append(nota)
	notasalumnos.append(listanotas)
	listanotas=[]
	cont=0

indice=0
for alumno in listaalumnos:
		print("Notas de %15s: %s \n" %(alumno,notasalumnos[indice]))
		indice+=1
