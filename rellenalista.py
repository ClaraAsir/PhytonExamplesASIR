#! /usr/bin/env python
# -*- encoding: utf-8 -*-
listanumeros=[]
# Creando lista con los números solicitados por teclado
num=input("Dame el número entero: ")
while num != "q":
    listanumeros.append(num)
    num=input("Dame el número entero: ")
# Recorrer listanumeros y mostrar
print("Números de lista: ")
for num in listanumeros:
    print(num)