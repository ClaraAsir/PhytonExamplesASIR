#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import os

def limpiar_pantalla():
    input("\nPulsa INTRO para continuar...")
    os.system('clear')
    
def menu():
    print("1. Sumar\n")
    print("2. Restar\n")
    print("3. Multiplicar\n")
    print("4. Dividir\n")
    print("5. Salir\n\n")
    opcion=input("Elige una opción: ")
    return opcion


def sumar(operador1,operador2):
    suma=operador1+operador2
    return suma


def restar(operador1,operador2):
    resta=operador1-operador2
    return resta


def multiplicar(operador1,operador2):
    mult=operador1*operador2
    return mult


def dividir(operador1,operador2):
    try:
        division=operador1/operador2
        return division
    except ZeroDivisionError:
        print("Disivión entre cero, no permitida")

try:
    op1=float(input("Indica el operador1: "))
    op2=float(input("Indica el operador2: "))
    opc=menu()
    #limpiar_pantalla()
    while opc != '5':
        if opc == '1':
            lasuma=sumar(op1,op2)
            print("%.2f + %.2f = %.2f" %(op1,op2,lasuma))
            limpiar_pantalla()
        if opc == '2':
            laresta=restar(op1,op2)
            print("%.2f - %.2f = %.2f" %(op1,op2,laresta))
            limpiar_pantalla()
        if opc == '3':
            lamult=multiplicar(op1,op2)
            print("%.2f x %.2f = %.2f" %(op1,op2,lamult))
            limpiar_pantalla()
        if opc == '4':
            ladiv=dividir(op1,op2)
            print("%.2f / %.2f = %.2f" %(op1,op2,ladiv))
            limpiar_pantalla()
        opc=menu()
except ValueError:
    print("Los operandos han de ser números reales")
    limpiar_pantalla()