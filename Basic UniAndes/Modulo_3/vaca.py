def hacer_la_vaca(salon, vaca):
    filas = len(salon)
    columnas = len(salon[0])
    
    total_dinero = 0
    estudiante_max = (0, 0)
    max_dinero = -1
    
    for i in range(filas):
        for j in range(columnas):
            total_dinero += salon[i][j]
            if salon[i][j] > max_dinero:
                max_dinero = salon[i][j]
                estudiante_max = (i, j)
    
    if vaca == 'botella':
        costo_vaca = 120000
    elif vaca == 'pastel':
        costo_vaca = 35000
    else:
        return ['No Alcanza']
    
    if total_dinero >= costo_vaca:
        return ['Hay Vaca', estudiante_max]
    else:
        return ['No Alcanza']

# Ejemplo de uso
salon = [
    [50000, 75000, 60000],
    [100000, 30000, 90000],
    [40000, 80000, 70000]
]

resultado = hacer_la_vaca(salon, 'pastel')
print(resultado)
