#!/usr/bin/env python
# -*- coding: utf-8 -*-

def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multi(x, y):
    return x * y

def divi(x, y):
    return x / y


print("***Calculator***")
print("1.Suma")
print("2.Resta")
print("3.Multiplicación")
print("4.División")
print("5.Salir")

while True:
    op = input("Elige una opción: ")
    if op in ('1', '2', '3', '4','5'):
        if op == '5':
            print ("Hasta luego")
            exit()
        try:
            num1 = float(input("Introduce un número: "))
            num2 = float(input("Introduce otro número: "))
        except ValueError:
            print("Número no válido")
            continue

        if op == '1':
            print(num1, "+", num2, "=", suma(num1, num2))

        elif op == '2':
            print(num1, "-", num2, "=", resta(num1, num2))

        elif op == '3':
            print(num1, "*", num2, "=", multi(num1, num2))

        elif op == '4':
            print(num1, "/", num2, "=", divi(num1, num2))
    else:
        print("Opción no válida")