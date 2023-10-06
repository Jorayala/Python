def letra_mas_comun(cadena):
   
    frecuencia_letras = {}
    
    
    for letra in cadena:
        if letra.isalpha():  
            if letra in frecuencia_letras:
                frecuencia_letras[letra] += 1
            else:
                frecuencia_letras[letra] = 1
    
    
    max_frecuencia = max(frecuencia_letras.values())
    letra_mas_comun = ''
    
    for letra, frecuencia in frecuencia_letras.items():
        if frecuencia == max_frecuencia:
            if not letra_mas_comun or letra > letra_mas_comun:
                letra_mas_comun = letra
    
    return letra_mas_comun


cadena = "Hola, cómo estás?cccc"
resultado = letra_mas_comun(cadena)
print("Letra más común:", resultado)
