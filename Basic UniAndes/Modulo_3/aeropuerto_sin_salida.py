def listar_aeropuertos_sin_salida(vuelos):
    # Crear un conjunto para almacenar los aeropuertos con vuelos de salida
    aeropuertos_con_salida = set()
    
    # Llenar el conjunto con los aeropuertos de salida
    for codigo_vuelo, info_vuelo in vuelos.items():
        origen = info_vuelo['origen']
        aeropuertos_con_salida.add(origen)
    
    # Crear un conjunto para almacenar los aeropuertos con vuelos de llegada
    aeropuertos_con_llegada = set()
    
    # Llenar el conjunto con los aeropuertos de llegada
    for codigo_vuelo, info_vuelo in vuelos.items():
        destino = info_vuelo['destino']
        aeropuertos_con_llegada.add(destino)
    
    # Encontrar los aeropuertos de llegada que no tienen vuelos de salida
    aeropuertos_sin_salida = aeropuertos_con_llegada - aeropuertos_con_salida
    
    return list(aeropuertos_sin_salida)

# Ejemplo de uso
vuelos = {
    'V1': {'aerolinea': 'AA', 'origen': 'JFK', 'destino': 'LAX', 'distancia': 2475, 'retraso': 15, 'duracion': 360, 'salida': 800},
    'V2': {'aerolinea': 'UA', 'origen': 'LAX', 'destino': 'SFO', 'distancia': 337, 'retraso': 0, 'duracion': 105, 'salida': 1200},
    'V3': {'aerolinea': 'DL', 'origen': 'JFK', 'destino': 'ATL', 'distancia': 760, 'retraso': 30, 'duracion': 150, 'salida': 930},
    'V4': {'aerolinea': 'AA', 'origen': 'DFW', 'destino': 'ORD', 'distancia': 802, 'retraso': 0, 'duracion': 150, 'salida': 1100},
    'V5': {'aerolinea': 'UA', 'origen': 'SFO', 'destino': 'LAX', 'distancia': 337, 'retraso': 0, 'duracion': 105, 'salida': 1400},
    'V6': {'aerolinea': 'DL', 'origen': 'ATL', 'destino': 'LGA', 'distancia': 762, 'retraso': 10, 'duracion': 160, 'salida': 1500},
    'V7': {'aerolinea': 'AA', 'origen': 'ORD', 'destino': 'DFW', 'distancia': 802, 'retraso': 0, 'duracion': 150, 'salida': 1600},
}

aeropuertos_sin_salida = listar_aeropuertos_sin_salida(vuelos)
print("Aeropuertos sin vuelos de salida:", aeropuertos_sin_salida)
