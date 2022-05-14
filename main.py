import os
from pathlib import Path

#Se obtiene el ruta actual en la que se trabaja
directorio_actual = Path.cwd()
ruta_actual = Path(directorio_actual)

def menu():
    print ('¿Qué desea hacer?')
    print ('1) Listar documentos')
    print ('2) Leer documento')
    print ('3) Eliminar documento') 
    print ('4) Terminar consulta') 

def validacion_opciones():
    while True:
        entrada = input('Ingrese el número de la opción: ')
        try:
            entrada = int(entrada)
            return entrada;
        except ValueError:
            print ("La entrada es incorrecta; escribe un numero entero")

def listar_documentos():
    for documento in ruta_actual.iterdir():
    
        if documento.is_file() and  documento.suffix == '.txt':
            print(documento.name)

def leer_documentos():
    while True:
        nombre = input('¿Qué archivo quiere leer? (Nombre + .txt): ')
        ruta_documento = directorio_actual / nombre
        if ruta_documento.exists():
            with open(ruta_documento) as documento:
                archivo = documento.read()
                print(archivo)
                break
        else:
            print('El documento no existe')

def eliminar_documento():
    nombre = input('¿Qué archivo quiere eliminar?: ')
    ruta_documento = directorio_actual / nombre
    os.remove(ruta_documento)

def limpiar_pantalla():
    while True:
        continuar = (input('¿Quiere hacer otra consulta ? Si / No: '))
        if continuar.upper() == "SI":
            os.system('clear')
            break
        elif continuar.upper() == "NO":
            print('Fin de la consulta')
            exit()

menu()
eleccion = validacion_opciones()

while eleccion:
    if eleccion == 1:
        listar_documentos()
    elif eleccion == 2:
        leer_documentos()
    elif eleccion == 3:
        eliminar_documento()
    elif eleccion == 4:
        print ('Fin de la consulta')
        break
    limpiar_pantalla()
    menu()
    eleccion = validacion_opciones()