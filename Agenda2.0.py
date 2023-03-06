#   EMPIEZA A LEER POR LA LÍNEA 10, LA FUNCIÓN DEL MENÚ, Y SALTA A LA 75, QUE COMIENZA EL PROGRAMA.
#   AHÍ YA SOLO ES IR SIGUIENDO EL CÓDIGO


import os
import time

#   FUNCIONES ------------------------------------------------------------------

def menu():                                     # limpia la pantalla para que se vea solo
    os.system('clear')                          # el menú. input para meter la opcion
    print('1  CREAR')                           # en la variable op (como string) y retorna
    print('2  AGENDA')                          # el valor de op
    print('3  ELIMINA')
    print('4  GUARDA')
    print('5  BORRAR AGENDA')
    print('6  BACKUP')
    print('7  RECUPERA BACKUP')
    print('8  CARGAR AGENDA')
    print('Ss SALIR')
    op=input('\nOPCION: ')
    return op

def limpiar():
    input('\nPULSA INTRO...')
    os.system('clear')

def agregar(a,b):                               # hemos creado la agenda justo antes del programa (línea 73) y ahora
    agenda[a]=b                                 # recogemos el valor de nom y num en a y b ( menos nom y num como quieras llamarlos) 
                                                # metemos en agenda[key=nom] el valor=num 
def mostrar():                                      # recorremos agenda de 2 en 2 items, cada uno de sus key/values y se guardan en a y b
    for a,b in agenda.items():                      # mostramos con formato 1234567890:1234567890 
        print('%10s:%10s' %(a,b))                   # (si no pones %número solo ocupa lo que ocupe el texto)

def existe(a):                                  # metemos en a el valor de nom_e. 
    sapo=0                                      # ponemos el sapo a cero 
    for i in agenda.keys():                     # recorre con i los nombres(.keys()) de agenda
        if a==i:                                # si i es igual a a(que es = a nom_e)
            sapo=1                              # entonces el sapo se chiva
        else:                                   # y si no encuentra el nombre no se chiva
            sapo=0
    return sapo                                 # retornamos lo que diga el sapo

def guardar():
    f=open('file.txt','w')                      # convertimos el fichero file.txt en una variable en modo escritura
    for a,b in agenda.items():                  # recorremos la agenda de 2 en 2 key/valor y los vamos guardando en a y b
        f.writelines('%10s:%10s\n'%(a,b))       # en la variable-archivo f escribimos en lineas a y b en formato 1234567890:1234567890\n
    f.close()                                   # IMPORTANTÍSIMO CERRAR SIEMPRE QUE SE ABRE

def borrar():
    f=open('file.txt','w')                      # simplemente convertimos el fichero file.txt en una variable en modo escritura
    f.write('')                                 # y machacamos el contenido con nada escrito, en blanco
    f.close()                                   # SIEMPRE QUE ABRAS CIERRA, luego entremedias mete lo que sea

def backup():
    os.system('cat file.txt >> file.bkup.txt')  # usamos os para poder hacer una copia mediante comandos de linux
    
def rec_backup():
    os.system('cat file.bkup.txt >> file.txt')  # usamos os para hacer lo mismo que el backup pero en sentido opuesto

def rec():
    f=open('file.txt','r')                      # convertimos el fichero file.txt en una variable en modo LECTURA (y lo cerramos abajo)
    re=f.readlines()                            # en la variable re guardamos el contenido de files.txt leido línea a línea
    for i in re:                                # recorremos re guardando en i cada línea. i vale la primera línea ahora mismo
        sinsalto=i.replace('\n','')                 # quitamos los saltos de línea del final y lo guardamos en sinsalto
        mitad1=sinsalto[:10]                        # cortamos los 10 primeros carácteres de sinsalto y lo llamamos mitad1
        mitad2=sinsalto[11:21]                      # quitamos del 11 al 21 y lo llamamos mitad
        agenda[mitad1]=mitad2                       # guardamos en agenda[key=mitad1] el valor mitad2 (es un poco chusco pero funcional)
    f.close()

#   PROGRAMA ------------------------------------------------------------------

agenda={}

opcion=menu()                                                       # recoge en opcion el valor que retornaba la función menu(). 
opcion=opcion.lower()                                               # transforma la string en minúsculas
while opcion !='s':                                                 # mientras opcion sea distinto de s minúscula...
    try:
        if opcion=='1':
            os.system('clear')                                      # impiamos pantalla para que salga solo el menu
            nom=input('NOMBRE: ')                                   # introducimos nombre como string en nom
            num=input('NÚMERO: ')                                   # introducimos número como string en num
            agregar(nom,num)                                        # creamos la función agregar() (línea 28) con los parámetros nom y num
            limpiar()                                               # cuando acaba se queda esperando un intro para resetear

        if opcion=='2':
            os.system('clear')                                      # limpia la pantalla para mostrar lo que traiga la función
            mostrar()                                               # mostrar(), (línea 31) y lo muestra hasta que des intro
            limpiar()

        if opcion=='3':
            os.system('clear')                                      # limpia la pantalla y solo te pide el nombre a eliminar que mete en
            nom_e=input('NOMBRE: ')                                 # la variable nom_e. creamos la funcion para PREGUNTAR si existe y la
            sapo=existe(nom_e)                                      # RESPUESTA a esa pregunta la guarda en SAPO (línea 35)
            if sapo==1:                                             # ahora preguntamos a sapo si se chiva o no. si se chiva ...
                del agenda[nom_e]                                   # eliminamos de la agenda el nombre introducido en nom_e
                print('\nel contacto ha sido elimnado')
            else:                                                   # si no lo ha encontrado no elimina nada (obvio)
                print('\nel contacto no existe')
            limpiar()

        if opcion=='4':
            os.system('clear')                                      # si pulsamos la opcion 4 llama a la funcion guardar
            guardar()                                               # línea 44 
            print('AGENDA GUARDADA')                                # mensaje tranquilizador
            limpiar()                                               # limpia la pantalla cuando des al intro

        if opcion=='5':
            borrar()                                                # creamos la función de borrar (línea 50)
            limpiar()

        if opcion=='6':
            backup()                                                # creamos la función backup (línea 55)
            limpiar()

        if opcion=='7':
            rec_backup()                                            # creamos la función recuperar backup (línea 58)
            limpiar()

        if opcion=='8':
            rec()                                                   # creamos la función para cargar el archivo en la agenda (línea 61)
            limpiar()

        opcion=menu()                                               # PARA QUE NO ENTRE EN BUCLE INFINITO, vuelve al menú inicial
    except ValueError:
        print('error fatal de la muerte')
        limpiar()

while True:                                                 # esto es una chorrada para practicar con 
    for s in range(3,0,-1):                                 # rangos y el sleep del import.time
        os.system('clear')                                  # el mensaje de despedida SIEMPRE A LA ALTURA DEL WHILE DE INICIO
        print('...cerrando en %1d'%s)
        time.sleep(1)
    os.system('clear')    
    print('CHAO PESCAO')
    break