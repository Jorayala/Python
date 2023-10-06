def letra_mas_comun(cadena):
    # Eliminar espacios, puntos y comas de la cadena
    cadena_limpia = cadena.replace(" ", "").replace(".", "").replace(",", "")
    print(cadena_limpia)
    # Crear un diccionario para contar la frecuencia de cada letra
    frecuencia_letras = {}
    for letra in cadena_limpia:
        if letra in frecuencia_letras:
            frecuencia_letras[letra] += 1
        else:
            frecuencia_letras[letra] = 1
    
    # Encontrar la letra más común
    letra_mas_comun = max(frecuencia_letras, key=lambda letra: (frecuencia_letras[letra], letra))
    
    return letra_mas_comun

# Ejemplo de uso
cadena = "Hoy es un hermoso dia, lleno de sol y alegria."
resultado = letra_mas_comun(cadena)
print("La letra más común en la cadena es:", resultado)
