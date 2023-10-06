import random

def generar_imagen(filas, columnas):
    imagen = []
    for _ in range(filas):
        fila = []
        for _ in range(columnas):
            # Generar un valor de píxel aleatorio entre 0 y 255
            pixel = (random.randint(0, 255),)
            fila.append(pixel)
        imagen.append(tuple(fila))
    return imagen

# Tamaño de la imagen (filas x columnas)
filas = 5
columnas = 5

imagen_generada = generar_imagen(filas, columnas)

# Imprimir la imagen generada
for fila in imagen_generada:
    print(fila)
