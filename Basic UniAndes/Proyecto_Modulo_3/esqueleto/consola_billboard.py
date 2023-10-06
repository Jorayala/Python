#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ejercicio nivel 3: Billboard.
Interfaz basada en consola para la interacción con el usuario.

Temas:
* Instrucciones repetitivas.
* Listas
* Diccionarios
* Archivos

@author: Cupi2
"""

import billboard as bb

def ejecutar_cargar_canciones() -> list:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de
    las canciones y las carga.
    Retorno: list
        La lista de canciones con la información del archivo.
    """
    canciones = None
    archivo = input("Por favor ingrese el nombre del archivo CSV con las canciones: ")
    canciones = bb.cargar_canciones(archivo)
    if len(canciones) == 0:
        print("El archivo seleccionado no es válido. No se pudieron cargar las canciones del Ranking")
    else:
        print("Se cargaron", len(canciones), "canciones a partir del archivo.")
    return canciones

def ejecutar_buscar_cancion(canciones:list)->None:
    """ Ejecuta la opción de buscar una canción dado el nombre y el año del 
    ranking al cual pertenece 
    """
    cancion = input("Por favor ingrese el nombre de la canción que desea buscar: ")
    anio = int(input("Por favor ingrese el año de la canción que desea buscar: "))
    
    #TODO: complete el código haciendo el llamado a la función del módulo que
    #implementa este requrimiento e imprimiendo por pantalla el resultado
    
    
    # Llamado a la función que busca la canción
    resultado = bb.buscar_cancion_por_nombre_y_anio(canciones, cancion, anio)
    
    if resultado is not None:
        print("Resultado de la búsqueda:")
        print(resultado)
    else:
        print("La canción no fue encontrada.")


def ejecutar_canciones_anio(canciones:list)->None:
    """ Ejecuta la opción de consultar las canciones de un año dado 
    """
    anio = int(input("Por favor ingrese el año que desea consultar: "))

    #TODO: complete el código haciendo el llamado a la función del módulo que
    #implementa este requrimiento e imprimiendo por pantalla el resultado
    
    
    canciones_del_anio = bb.canciones_por_anio(canciones, anio)
    
    if not canciones_del_anio:
        print("No se encontraron canciones para el año ingresado.")
    else:
        print("Canciones del año {}:".format(anio))
        for cancion in canciones_del_anio:
            print("Posición: {}, Canción: {}, Artista: {}".format(cancion['posicion'], cancion['nombre_cancion'], cancion['nombre_artista']))


    
def ejecutar_canciones_artista_periodo(canciones:list)->None:
    """ Ejecuta la opción de consultar las canciones de un artista dado en 
    un periodo de tiempo definido 
    """
    artista = input("Por favor ingrese el nombre del artista que desea buscar: ")
    anio_inic = int(input("Por favor ingrese el año inicial que desea buscar: "))
    anio_fin = int(input("Por favor ingrese el año final que desea buscar: "))

    #TODO: complete el código haciendo el llamado a la función del módulo que
    #implementa este requrimiento e imprimiendo por pantalla el resultado
    canciones_del_artista = bb.canciones_por_artista_y_periodo(canciones, artista, anio_inic, anio_fin)
    
    if not canciones_del_artista:
        print("No se encontraron canciones para el artista en el período especificado.")
    else:
        print("Canciones del artista en el período:")
        for cancion in canciones_del_artista:
            print(f"Posición: {cancion['posicion']}, Nombre: {cancion['nombre_cancion']}, Año: {cancion['anio']}")
    
def ejecutar_todas_canciones_artista(canciones:list)->None:
    """ Ejecuta la opción de consultar todas las canciones de un artista dado 
    """
    artista = input("Por favor ingrese el nombre del artista que desea buscar: ")

    #TODO: complete el código haciendo el llamado a la función del módulo que
    #implementa este requrimiento e imprimiendo por pantalla el resultado

    
    canciones_del_artista = bb.canciones_por_artista(canciones, artista)
    
    if not canciones_del_artista:
        print("No se encontraron canciones para el artista especificado.")
    else:
        print(f"Canciones de {artista}:")
        for cancion in canciones_del_artista:
            print(f"Posición: {cancion['posicion']}, Nombre: {cancion['nombre_cancion']}, Año: {cancion['anio']}")

def ejecutar_todos_artistas_cancion(canciones:list)->None:
    """ Ejecuta la opción de consultar todos los artistas que han interpretado 
    una canción dada 
    """
    min = input("Por favor ingrese el nombre de la canción que desea buscar: ")

    #TODO: complete el código haciendo el llamado a la función del módulo que
    #implementa este requrimiento e imprimiendo por pantalla el resultado

    artistas_interpretes = bb.artistas_de_cancion(canciones, min)
    
    if not artistas_interpretes:
        print("No se encontraron artistas para la canción especificada.")
    else:
        print(f"Artistas que han interpretado {min}:")
        for artista in artistas_interpretes:
            print(artista)

def ejecutar_artistas_mas_populares(canciones:list)->None:
    """ Ejecuta la opción de consultar los artistas más populares 
    """
    min = input("Por favor ingrese la cantidad mínima de canciones que desea buscar: ")

    #TODO: complete el código haciendo el llamado a la función del módulo que
    #implementa este requrimiento e imprimiendo por pantalla el resultado
    artistas_populares = bb.artistas_mas_productivos(canciones, min)
    
    if artistas_populares:
        print("Artistas más populares:")
        for artista, cantidad in artistas_populares.items():
            print(f"{artista}: {cantidad} canciones")
    else:
        print("No se encontraron artistas populares con la cantidad mínima especificada.")

     
def ejecutar_artista_estrella(canciones:list)->None:
    """ Ejecuta la opción de consultar el artista estrella de todos los tiempos 
    """
    #TODO: complete el código haciendo el llamado a la función del módulo que
    #implementa este requrimiento e imprimiendo por pantalla el resultado
    artista_estrella = bb.artista_mas_productivo(canciones)
    
    if artista_estrella:
        for artista, cantidad in artista_estrella.items():
            print(f"El artista estrella de todos los tiempos es: {artista} con {cantidad} canciones")
    else:
        print("No se encontró un artista estrella.")


def ejecutar_artistas_y_sus_canciones(canciones:list)->None:
    """ Ejecuta la opción de consultar la lista completa de artistas del Billboard 
    junto con sus canciones 
    """
    #TODO: complete el código haciendo el llamado a la función del módulo que
    #implementa este requrimiento e imprimiendo por pantalla el resultado

    artistas_con_canciones = bb.canciones_por_artista_dict(canciones)
    
    for artista, canciones in artistas_con_canciones.items():
        print(f"Artista: {artista}")
        print(f"Canciones: {', '.join(canciones)}")
        print("=" * 30)

def ejecutar_promedio_canciones_por_artista(canciones:list)->None:
    """ Ejecuta la opción de consultar la cantidad promedio de canciones que los 
    artistas tienen en el listado de Billboard 
    """
    #TODO: complete el código haciendo el llamado a la función del módulo que
    #implementa este requrimiento e imprimiendo por pantalla el resultado

    promedio = bb.promedio_canciones_por_artista(canciones)
    print(f"La cantidad promedio de canciones por artista es: {promedio:.2f}")
    
    
def mostrar_menu():
    """Imprime las opciones de ejecución disponibles para el usuario.
    """
    print("\nOpciones")
    print("1. Cargar un archivo de canciones")
    print("2. Buscar una canción")
    print("3. Consultar las canciones de un año")
    print("4. Consultar las canciones de un artista en un periodo")
    print("5. Consultar todas las canciones de un artista")
    print("6. Consultar todos los artistas que han interpretado una canción")
    print("7. Consultar los artistas más populares")
    print("8. Consultar el artista estrella de todos los tiempos")
    print("9. Consultar los artistas y sus canciones")    
    print("10. Consultar la cantidad promedio de canciones por artista")
    print("11. Salir.")

def iniciar_aplicacion():
    """Ejecuta el programa para el usuario."""
    continuar = True
    canciones = list()
    while continuar:
        mostrar_menu()
        opcion_seleccionada = int(input("Por favor seleccione una opción: "))
        if opcion_seleccionada == 1:
            canciones=ejecutar_cargar_canciones()
        elif opcion_seleccionada == 2:
            ejecutar_buscar_cancion(canciones)
        elif opcion_seleccionada == 3:
            ejecutar_canciones_anio(canciones)
        elif opcion_seleccionada == 4:
            ejecutar_canciones_artista_periodo(canciones)
        elif opcion_seleccionada == 5:
            ejecutar_todas_canciones_artista(canciones)
        elif opcion_seleccionada == 6:
            ejecutar_todos_artistas_cancion(canciones)
        elif opcion_seleccionada == 7:
            ejecutar_artistas_mas_populares(canciones)
        elif opcion_seleccionada == 8:
            ejecutar_artista_estrella(canciones)
        elif opcion_seleccionada == 9:
            ejecutar_artistas_y_sus_canciones(canciones)
        elif opcion_seleccionada == 10:
            ejecutar_promedio_canciones_por_artista(canciones)            
        elif opcion_seleccionada == 11:
            continuar = False
        else:
            print("Por favor seleccione una opción válida.")

#PROGRAMA PRINCIPAL
iniciar_aplicacion()

