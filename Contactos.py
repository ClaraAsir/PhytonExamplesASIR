
'''
Crea un script llamado ejer1tunombre.py que muestre el siguiente
menú, hasta pulsar la opción de salir:
1. Usuarios actuales con uid mayor o igual a 1000 y guardar
2. Grupos actuales con gid mayor o igual a 1000 y guardar
3. Crear nuevo grupo
4. Crear nuevo usuario
5. Hacer miembro de un grupo a un usuario
6. Eliminar usuario dado su nombre
7. Eliminar grupo dado su nombre
S/s. Salir
'''

'''
1. Usuarios actuales con uid mayor o igual a 1000 y guardar.- Mostrará por
pantalla todos los usuarios cuyo uid sea mayor o igual a 1000 y los guardará en un
fichero llamado listadousuarios.txt.
En cada una de las líneas de dicho fichero deberá aparecer únicamente el nombre
del usuario y su uid.
Caso de existir el archivo, se borrará su contenido y se escribirá nuevamente.
'''

'''
2. Grupos actuales con gid mayor o igual a 1000 y guardar.- Mostrará por
pantalla todos los grupos cuyo gid sea mayor o igual a 1000 y los guardará en un
fichero llamado listadogrupos.txt.
En cada una de las líneas deberá aparecer únicamente el nombre del grupo y su
gid.
Caso de existir el archivo, se borrará su contenido y se escribirá nuevamente.
'''

'''
3. Crear nuevo grupo: Se llamará a una función que recibirá como parámetros
el nombre del grupo y su gid, introducidos previamente por teclado. Dicha función
creará dicho grupo con el gid pasado.
'''

'''
4. Crear nuevo usuario: Se llamará a una función que recibirá como parámetros
el nombre del usuario, grupo principal y su uid, introducidos previamente por
teclado. Primero, la función comprobará si existe el grupo entonces creará dicho
usuario con el uid pasado y con el grupo principal pasado. Caso de no existir el
grupo mostrará el mensaje correspondiente y no creará nada.
'''

'''
5. Hacer miembro de un grupo a un usuario: Se llamará a una función que
recibirá como parámetros el nombre del grupo y el del usuario. Comprobará si
existe el grupo, caso contrario se lanzará mensaje y no se hará nada. Si existe el
grupo pero no el usuario, éste último se creará y su grupo principal será el grupo
pasado, si no (caso de existir también el usuario) se le hará miembro de dicho
grupo.
'''

'''
6. Eliminar usuario, dado su nombre. : Pedirá el nombre de usuario a eliminar
y, llamará la función existe_usuario (que recibirá como parámetro el nombre de
usuario) y devolverá si existe. Caso de existir llamará a la función eliminar_usuario
(que recibirá como parámetro el nombre de usuario) y eliminará el dicho usuario
con todo su directorio.
'''

'''
7. Eliminar grupo, dado su nombre. : Pedirá el nombre del grupo a eliminar y,
llamará la función existe_grupo (que recibirá como parámetro el nombre del
grupo) y devolverá si existe. Caso de existir llamará a la función eliminar_grupo
(que recibirá como parámetro el nombre del grupo) y eliminará el dicho grupo del
sistema.
'''


import os

def menu():
    os.system('clear')
    print('1. Usuarios actuales con uid mayor o igual a 1000 y guardar')
    print('2. Grupos actuales con gid mayor o igual a 1000 y guardar')
    print('3. Crear nuevo grupo')
    print('4. Crear nuevo usuario')
    print('5. Hacer miembro de un grupo a un usuario')
    print('6. Eliminar usuario dado su nombre')
    print('7. Eliminar grupo dado su nombre')
    print('S/s. Salir') 
    op=input('\nElige una opción: ')
    return op
    
def limpiar():
    input('\npulsa intro...')
    os.system('clear')


lista=[]
lista1=[]


opcion=menu()                                                           # recogemos el valor de op en la función de menú()
opcion=opcion.lower()                                                   # convertimos su string interna en minúsculas
while opcion !='s':                                                     # mientras sea distinta de s...
    try:
        if opcion=='1':     
            os.system('clear')
            os.system('cut -d: -f1,3 /etc/passwd > lista.txt')          # en los bloques separados por : cogemos el primero y el tercero
            os.system('chmod 777 lista.txt')                            # y los enviamos a lista.txt. damos permisos a lista.txt
            f=open('lista.txt','r')                                     # abrimos en modo lectura lista.txt y lo convertimos en variable (cierra en 117)
            ff=open('listadousuarios.txt','w')                          # hacemos lo mismo con listadousuarios pero en modo escritura (cierra en 118)
            lista=f.readlines()                                         # metemos en lista el contenido de lista.txt leido línea a línea (ahora es una lista)
            for i in lista:                                             # recorremos el contenido de lista.txt (cada linea es así ["usuario:uid\n"])
                sinsalto=i.replace('\n','')                             # reemplazamos el salto de línea (ahora se vería así ["usuario:uid"])
                mitad=sinsalto.split(':')                               # separamos por : (ahora se vería así ["usuario","uid"])
                num=int(mitad[1])                                       # dentro de num cogemos el índice 1(uid) y lo convertimos en numeral
                if num>1000:                                            # comparamos el uid con el número que nos han pedido
                    ff.writelines(i)                                    # si coincie se escribe la línea entera (i = ["usuario:uid\n"]) en ff = listadousuarios.txt
                    print(i)                                            # ademas se muestra por pantalla ["usuario:uid\n"]
                                                                        # esto lo hace hasta que recorra todas las líneas
            print(lista)
            f.close()                                                   # cierra lista.txt
            ff.close()                                                  # cierra listadousuarios.txt
            limpiar()

        if opcion=='2':                                                 # LO MISMO QUE EL EJERCICIO ANTERIOR PERO COGIENDO EL CAMPO 4 EN VEZ DEL 3
            os.system('clear')                                          # EN EL COMANDO DE CUT. CAMBIANDO LOS NOMBRES DE LOS FICHEROS 
            print('\nOPCIÓN 2\n')
            os.system('cut -d":" -f 1,4 /etc/passwd > lista1.txt')
            os.system('chmod 777 lista1.txt')
            f=open('lista1.txt','r')
            ff=open('listadogrupos.txt','w')
            lista1=f.readlines()
            for i in lista1:
                sinsalto=i.replace('\n','')
                poritems=sinsalto.split(':')
                uid=int(poritems[1])
                if uid>1000:
                    ff.writelines(i)
                    print(i)
            f.close()
            ff.close()
            limpiar()
            
        if opcion=='3':                         # no hago estos puntos porque bñasicamente son usar os y 
            print('\nOPCIÓN 1\n')               # comandos de linux.
        if opcion=='4':
            print('\nOPCIÓN 1\n')
        if opcion=='5':
            print('\nOPCIÓN 1\n')
        if opcion=='6':
            print('\nOPCIÓN 1\n')
        if opcion=='7':
            print('\nOPCIÓN 1\n')
        opcion=menu()

    except ValueError:
        print('error fatal')
        limpiar()

print('Adiós...')
