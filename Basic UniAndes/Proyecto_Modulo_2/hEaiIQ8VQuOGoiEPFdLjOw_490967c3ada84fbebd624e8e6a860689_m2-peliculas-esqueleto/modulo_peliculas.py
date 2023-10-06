"""
Ejercicio nivel 2: Agenda de peliculas.
Módulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
@author: Cupi2

NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MODULO:
        Los diccionarios de pelicula tienen las siguientes parejas de clave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que día de la semana se planea ver la película
"""

def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, 
                  clasificacion: str, hora: int, dia: str) -> dict:
    """Crea un diccionario que representa una nueva película con toda su información 
       inicializada.
    Parámetros:
        nombre (str): Nombre de la pelicula agendada.
        genero (str): Generos de la pelicula separados por comas.
        duracion (int): Duracion en minutos de la pelicula
        anio (int): Anio de estreno de la pelicula
        clasificacion (str): Clasificacion de restriccion por edad
        hora (int): Hora a la cual se planea ver la pelicula, esta debe estar entre 
                    0 y 2359
        dia (str): Dia de la semana en el cual se planea ver la pelicula.
    Retorna:
        dict: Diccionario con los datos de la pelicula
    """    
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    return  {
            "nombre": nombre,
            "genero": genero,
            "duracion": duracion,
            "anio": anio,
            "clasificacion": clasificacion,
            "hora": hora,
            "dia": dia
        }

def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict,  p5: dict) -> dict:
    """Encuentra en cual de los 5 diccionarios que se pasan por parametro esta la 
       pelicula cuyo nombre es dado por parametro.
       Si no se encuentra la pelicula se debe retornar None.
    Parametros:
        nombre_pelicula (str): El nombre de la pelicula que se desea encontrar.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: Diccionario de la pelicula cuyo nombre fue dado por parametro. 
        None si no se encuentra una pelicula con ese nombre.
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    if p1.get("nombre") == nombre_pelicula:
        return p1
    elif p2.get("nombre") == nombre_pelicula:
        return p2
    elif p3.get("nombre") == nombre_pelicula:
        return p3
    elif p4.get("nombre") == nombre_pelicula:
        return p4
    elif p5.get("nombre") == nombre_pelicula:
        return p5
    else:
        return None
    

def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    """Encuentra la pelicula de mayor duracion entre las peliculas recibidas por
       parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: El diccionario de la pelicula de mayor duracion
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    max_pelicula = p1
    
    if p2.get("duracion", 0) > max_pelicula.get("duracion", 0):
        max_pelicula = p2
    if p3.get("duracion", 0) > max_pelicula.get("duracion", 0):
        max_pelicula = p3
    if p4.get("duracion", 0) > max_pelicula.get("duracion", 0):
        max_pelicula = p4
    if p5.get("duracion", 0) > max_pelicula.get("duracion", 0):
        max_pelicula = p5

    return max_pelicula
    

def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:
    """Calcula la duracion promedio de las peliculas que entran por parametro. 
       Esto es, la duración total de todas las peliculas dividida sobre el numero de peliculas. 
       Retorna la duracion promedio en una cadena de formato 'HH:MM' ignorando los posibles decimales.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        str: la duracion promedio de las peliculas en formato 'HH:MM'
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    total_minutos = p1.get("duracion", 0) + p2.get("duracion", 0) + p3.get("duracion", 0) + p4.get("duracion", 0) + p5.get("duracion", 0)
    
    # Cálculo del promedio
    promedio_minutos = total_minutos // 5
    
    # Conversión a formato HH:MM
    horas = promedio_minutos // 60
    minutos = promedio_minutos % 60
    resultado = "{:02d}:{:02d}".format(horas, minutos)

    return resultado
    

def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    """Busca entre las peliculas cuales tienen como anio de estreno una fecha estrictamente
       posterior a la recibida por parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        anio (int): Anio limite para considerar la pelicula como estreno.
    Retorna:
        str: Una cadena con el nombre de la pelicula estrenada posteriormente a la fecha recibida. 
        Si hay mas de una pelicula, entonces se retornan los nombres de todas las peliculas 
        encontradas separadas por comas. Si ninguna pelicula coincide, retorna "Ninguna".
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    peliculas_posteriores = []
    
    if p1.get("anio", 0) > anio:
        peliculas_posteriores.append(p1.get("nombre", ""))
    
    if p2.get("anio", 0) > anio:
        peliculas_posteriores.append(p2.get("nombre", ""))
        
    if p3.get("anio", 0) > anio:
        peliculas_posteriores.append(p3.get("nombre", ""))
        
    if p4.get("anio", 0) > anio:
        peliculas_posteriores.append(p4.get("nombre", ""))
        
    if p5.get("anio", 0) > anio:
        peliculas_posteriores.append(p5.get("nombre", ""))
    
    # Comprobamos si encontramos películas posteriores al año indicado
    if peliculas_posteriores:
        return ", ".join(peliculas_posteriores)
    else:
        return "Ninguna"

    

def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    """Indica cuantas peliculas de clasificación '18+' hay entre los diccionarios recibidos.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        int: Numero de peliculas con clasificacion '18+'
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    return (p1.get('clasificacion') == '18+') + \
           (p2.get('clasificacion') == '18+') + \
           (p3.get('clasificacion') == '18+') + \
           (p4.get('clasificacion') == '18+') + \
           (p5.get('clasificacion') == '18+')
    

def reagendar_pelicula(peli:dict, nueva_hora: int, nuevo_dia: str, 
                       control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->bool: 
    """Verifica si es posible reagendar la pelicula que entra por parametro. Para esto verifica
       si la nueva hora y el nuevo dia no entran en conflicto con ninguna otra pelicula, 
       y en caso de que el usuario haya pedido control horario verifica que se cumplan 
       las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula a reagendar
        nueva_hora (int): Nueva hora a la cual se quiere ver la pelicula
        nuevo_dia (str): Nuevo dia en el cual se quiere ver la pelicula
        control_horario (bool): Representa si el usuario quiere o no controlar
                                el horario de las peliculas.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        bool: True en caso de que se haya podido reagendar la pelicula, False de lo contrario.
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    if peli != p1 and p1.get('hora') == nueva_hora and p1.get('dia') == nuevo_dia:
        return False
    if peli != p2 and p2.get('hora') == nueva_hora and p2.get('dia') == nuevo_dia:
        return False
    if peli != p3 and p3.get('hora') == nueva_hora and p3.get('dia') == nuevo_dia:
        return False
    if peli != p4 and p4.get('hora') == nueva_hora and p4.get('dia') == nuevo_dia:
        return False
    if peli != p5 and p5.get('hora') == nueva_hora and p5.get('dia') == nuevo_dia:
        return False

  

    return True

    
def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool)->bool:
    """Verifica si es posible invitar a la persona cuya edad entra por parametro a ver la 
       pelicula que entra igualmente por parametro. 
       Para esto verifica el cumplimiento de las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula que se desea ver con el invitado
        edad_invitado (int): Edad del invitado con quien se desea ver la pelicula
        autorizacion_padres (bool): Indica si el invitado cuenta con la autorizacion de sus padres 
        para ver la pelicula
    Retorna:
        bool: True en caso de que se pueda invitar a la persona, False de lo contrario.
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    clasificacion = peli.get("clasificacion")
    
    if clasificacion == "18+":
        return edad_invitado >= 18

    if clasificacion == "12+":
        return edad_invitado >= 12 or (edad_invitado < 12 and autorizacion_padres)

    
    return True
    









