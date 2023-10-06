import pandas as pd

def calcular_estadisticas(df):
    # Filtrar el DataFrame para incluir solo las filas donde el pago es mayor que cero
    df_filtrado = df[df['PAGO'] > 0]
    
    # Agrupar por modelo y calcular las estadísticas requeridas
    estadisticas = df_filtrado.groupby('MODELO').agg(
        CANTIDAD=('MODELO', 'size'),
        PROMEDIO=('PAGO', 'mean'),
        MAXIMO=('PAGO', 'max'),
        MINIMO=('PAGO', 'min'),
        ESTRELLAS=('ESTRELLAS', 'mean'),
        DESV.ESTRELLAS=('ESTRELLAS', 'std'),
        COMENTARIOS=('COMENTARIO', 'sum')
    )
    
    # Redondear los números a dos cifras decimales
    estadisticas = estadisticas.round(2)
    
    # Reemplazar NaN en DESVESTRELLAS con 0.0
    estadisticas['DESV.ESTRELLAS'].fillna(0.0, inplace=True)
    
    # Ordenar el índice (nombres de los modelos) en orden alfabético
    estadisticas.sort_index(inplace=True)
    
    return estadisticas

# Crear el DataFrame jave
jave = pd.DataFrame({
    'MODELO': ['Bus urbano #27', 'Silla tipo bar', 'piano', 'Fuente con flores', 'Bus urbano #27', 'Puesto de Yogurth', 'Playground', 'Bus urbano #27'],
    'USUARIO': ['Pedro', 'Juan', 'Ramiro', 'Daniel', 'Juan', 'Casemiro', 'Pedro', 'Ramiro'],
    'PAGO': [24.99, 4.99, 4.99, 0, 12, 0, 14, 0],
    'ESTRELLAS': [5, 3.5, 3.5, 5, 4, 5, 4.5, 1],
    'COMENTARIO': [True, False, False, True, True, True, True, True]
})

print(jave)
# Calcular las estadísticas y mostrar el resultado
resultado = calcular_estadisticas(jave)
print(resultado)
