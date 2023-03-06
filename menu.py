#! /usr/bin/env python
# -*- encoding: utf-8 -*-

def menu():
    print("1. Crear lista")
    print("2. Suma lista")
    print("3. Lista cuadrados")
    print("4. Salir")
    opcion=input("\nIndica la opción deseada: ")
    return(opcion)

def mostrar_lista(list):
    for n in list:
        print(n)

def crear_lista(num):
    lista.append(num)
   
def lista_cuadrados(list):
    listcuadrados=[]
    for ele in list:
        listcuadrados.append(ele**2)
    return listcuadrados
    
def suma(list):
    suma=0
    for ele in list:
        suma+=ele
    return(suma)
    
    
lista=[]
op=''

while op != '4':
    if op == '1':
        try:
            for n in range(1,5):
                numero=int(input("Dame un número entero: "))
                crear_lista(numero)
            print("\n\n\nLos elementos de la lista son: ")
            mostrar_lista(lista)
            print("\n\n") 
        except ValueError:
            print("El valor introducido no es un número entero")
    elif op == '2':
        lasuma=suma(lista)
        print("\n\nLa suma de los elementos de la lista es: %d" % lasuma)
        print("\n\n")       
    elif op == '3':
        lalistacuadrados=lista_cuadrados(lista)
        print("\n\n\nLos elementos de la lista son: ")
        mostrar_lista(lalistacuadrados)
        print("\n\n") 
    op=menu()
print("Adiós")