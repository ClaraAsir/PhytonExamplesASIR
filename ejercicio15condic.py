#! /usr/bin/env python
# -*- encoding: utf-8 -*-

contador=1
listanotas=[]
notasalumnos={}
cont=0
tuplanotas=('ISO','FH','LM','REDES')

while contador < 6:
	nombrealumno=input("Introduce el nombre del alumno: ")
	while cont < len(tuplanotas):
		nota=input("Alumno %15s. Nota de %5s: " %(nombrealumno,tuplanotas[cont]))
		cont+=1
		listanotas.append(nota)
	notasalumnos[nombrealumno]=listanotas
	listanotas=[]
	contador+=1
	cont=0



for alumno,notas in notasalumnos.items():
	print("Notas de %15s fueron:  " % alumno)
	for nota in notas:
		print(nota,end=" ")
	print('\n')
