def cargar_canciones(nombre_archivo):
    canciones = []

    with open(nombre_archivo, 'rb') as archivo:  # Cambio a 'rb'
        # Descartar la primera línea con las etiquetas de columna
        archivo.readline()
        for linea in archivo:
            campos = linea.strip().decode('utf-8').split(',')  # Decodificar el binario
            cancion = {
                'posicion': int(campos[0]),
                'nombre_cancion': campos[1],
                'nombre_artista': campos[2],
                'anio': int(campos[3]),
                'letra': campos[4]
            }
            canciones.append(cancion)
    
    return canciones



def buscar_cancion_por_nombre_y_anio(canciones, nombre_cancion, anio):
    for cancion in canciones:
        if cancion['nombre_cancion'] == nombre_cancion and cancion['anio'] == anio:
            return cancion
    return None

def canciones_por_anio(canciones, anio):
    canciones_del_anio = []
    
    for cancion in canciones:
        if cancion['anio'] == anio:
            cancion_sin_letra = {
                'posicion': cancion['posicion'],
                'nombre_cancion': cancion['nombre_cancion'],
                'nombre_artista': cancion['nombre_artista'],
                'anio': cancion['anio']
            }
            canciones_del_anio.append(cancion_sin_letra)
    
    return canciones_del_anio

def canciones_por_artista_y_periodo(canciones, artista, anio_inicial, anio_final):
    canciones_del_artista = []
    
    for cancion in canciones:
        if cancion['nombre_artista'] == artista and anio_inicial <= cancion['anio'] <= anio_final:
            cancion_sin_letra = {
                'posicion': cancion['posicion'],
                'nombre_cancion': cancion['nombre_cancion'],
                'nombre_artista': cancion['nombre_artista'],
                'anio': cancion['anio']
            }
            canciones_del_artista.append(cancion_sin_letra)
    
    return canciones_del_artista

def canciones_por_artista(canciones, artista):
    canciones_del_artista = []
    
    for cancion in canciones:
        if cancion['nombre_artista'] == artista:
            cancion_sin_letra = {
                'posicion': cancion['posicion'],
                'nombre_cancion': cancion['nombre_cancion'],
                'nombre_artista': cancion['nombre_artista'],
                'anio': cancion['anio']
            }
            canciones_del_artista.append(cancion_sin_letra)
    
    return canciones_del_artista

def artistas_de_cancion(canciones, cancion_busqueda):
    artistas_interpretes = []
    
    for cancion in canciones:
        if cancion['nombre_cancion'] == cancion_busqueda:
            artistas_interpretes.append(cancion['nombre_artista'])
    
    return artistas_interpretes

def artistas_mas_productivos(canciones, cantidad_minima):
    cantidad_minima = int(cantidad_minima)
    artistas_cantidad = {}
    
    for cancion in canciones:
        nombre_artista = cancion['nombre_artista']
        if nombre_artista in artistas_cantidad:
            artistas_cantidad[nombre_artista] += 1
        else:
            artistas_cantidad[nombre_artista] = 1
    
    artistas_seleccionados = {}
    for artista, cantidad in artistas_cantidad.items():
        if cantidad > cantidad_minima:
            artistas_seleccionados[artista] = cantidad
    
    return artistas_seleccionados

def artista_mas_productivo(canciones):
    artistas_cantidad = {}
    
    for cancion in canciones:
        nombre_artista = cancion['nombre_artista']
        if nombre_artista in artistas_cantidad:
            artistas_cantidad[nombre_artista] += 1
        else:
            artistas_cantidad[nombre_artista] = 1
    
    artista_mas_productivo = max(artistas_cantidad, key=artistas_cantidad.get)
    cantidad_canciones = artistas_cantidad[artista_mas_productivo]
    
    return {artista_mas_productivo: cantidad_canciones}

def canciones_por_artista_dict(canciones):
    artistas_canciones = {}
    
    for cancion in canciones:
        nombre_artista = cancion['nombre_artista']
        nombre_cancion = cancion['nombre_cancion']
        
        # Agregar la canción al diccionario del artista
        if nombre_artista in artistas_canciones:
            if nombre_cancion not in artistas_canciones[nombre_artista]:
                artistas_canciones[nombre_artista].append(nombre_cancion)
        else:
            artistas_canciones[nombre_artista] = [nombre_cancion]
    
    return artistas_canciones



def promedio_canciones_por_artista(canciones):
    artistas = set()
    canciones_unicas = set()
    
    for cancion in canciones:
        artistas.add(cancion['nombre_artista'])
        canciones_unicas.add(cancion['nombre_cancion'])
    
    cantidad_artistas = len(artistas)
    cantidad_canciones = len(canciones_unicas)
    
    if cantidad_artistas > 0:
        promedio = cantidad_canciones / cantidad_artistas
        return promedio
    else:
        return 0
