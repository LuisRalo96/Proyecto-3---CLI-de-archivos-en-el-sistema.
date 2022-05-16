import os
from pathlib import Path

# Se obtiene el ruta actual en la que se trabaja
directorio_actual = Path.cwd()
ruta_actual = Path(directorio_actual)

def menu():
    print ('¿Qué desea hacer?')
    print ('1) Listar documentos')
    print ('2) Leer documento')
    print ('3) Eliminar documento') 
    print ('4) Terminar consulta') 

# Valida que el valor ingresado por el usuario sea un número 
def validacion_opciones():
    while True:
        entrada = input('Ingrese el número de la opción: ')
        try:
            entrada = int(entrada)
            return entrada;
        except ValueError:
            print ("La entrada es incorrecta; escribe un numero entero")

# Muestra los documentos existentes con extensión .txt
def listar_documentos():
    for documento in ruta_actual.iterdir():
    
        if documento.is_file() and  documento.suffix == '.txt':
            print(documento.name)

""" 
Muestra el contenido del documento .txt solitado, 
además de validar que el usuario haya ingresado el nombre de un documento existente
"""
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

"""Elimina el documento solicitado,  
además de validar que el usuario haya ingresado el nombre de un documento existente
"""
def eliminar_documento():
    while True:
        nombre = input('¿Qué archivo quiere eliminar? (Nombre + .txt): ')
        ruta_documento = directorio_actual / nombre
        if ruta_documento.exists():
            os.remove(ruta_documento)
            break
        else:
            print('El documento no existe')

"""
Valida si el usuario quiere continuar con la consulta, 
si el usuario desea continuar, la pantalla se limpia en automático,
de lo contrario termina la ejecución del programa
"""
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

"""
Muestra el menú en un ciclo constante hasta que el usuario decida terminar la consulta
"""
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
