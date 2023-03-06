#! /usr/bin/env python
# -*- encoding: utf-8 -*-

listanum=[]
num=input("Dame un número entero: ")
while num != 'q':
	try:
			listanum.append(int(num))
			num=input("Dame un número entero: ")
	except ValueError:
		print("Valor introducido incorrecto")
		break

for numero in listanum:
	print(numero,end=" ")
		
		
