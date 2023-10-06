
nombre_materia_1 = "sociales"
nombre_materia_2 = "idiomas"
nombre_materia_3 = "filosofia"

def conteo_de_materias (nombre_materia_1:str, nombre_materia_2:str, nombre_materia_3:str)-> int:
    numero_materias = 0
    if "programacion" in nombre_materia_1: 
        numero_materias += 1
    if "matematica" in nombre_materia_1:
        numero_materias += 1
    if "filosofia" in nombre_materia_1:
        numero_materias += 1
    if "literatura" in nombre_materia_1:
        numero_materias += 1

    if "programacion" in nombre_materia_2: 
        numero_materias += 1
    if "matematica" in nombre_materia_2:
        numero_materias += 1
    if "filosofia" in nombre_materia_2:
        numero_materias += 1
    if "literatura" in nombre_materia_2:
        numero_materias += 1

    if "programacion" in nombre_materia_3: 
        numero_materias += 1
    if "matematica" in nombre_materia_3:
        numero_materias += 1
    if "filosofia" in nombre_materia_3:
        numero_materias += 1
    if "literatura" in nombre_materia_3:
        numero_materias += 1   

    return numero_materias

print(conteo_de_materias(nombre_materia_1, nombre_materia_2, nombre_materia_3))    