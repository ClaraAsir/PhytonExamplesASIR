#! /usr/bin/env python
# -*- encoding: utf-8 -*-
listanum=[3,4,65,78,13,0,1]
listaimpares=[]
# Creando lista con los números pares de listanum
for num in listanum:
    if num%2 != 0:
        listaimpares.append(num)
# Recorre lista pares y mostrar
print("Lista de números impares: ")
for num in listaimpares:
    print(num)