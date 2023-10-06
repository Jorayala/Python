# Crear una matriz 5x5 con todas las casillas en 0
matriz = [[0 for _ in range(5)] for _ in range(5)]
print(matriz)
# Rellenar la diagonal principal con 1
for i in range(5):
    matriz[i][i] = 1

# Imprimir la matriz resultante
for fila in matriz:
    print(fila)
