def leer_csv(nombre_archivo):
    diccionario_datos = {}
    
    archivo_csv = open(nombre_archivo, 'r', encoding='ISO-8859-1')
    lineas = archivo_csv.readlines()
    archivo_csv.close()
    print(lineas)
    
    encabezados = lineas[0].strip().split(',')

    print(encabezados)
    
    for linea in lineas[1:]:
        valores = linea.strip().split(',')
        diccionario = {}
        for i in range(len(encabezados)):
            diccionario[encabezados[i]] = valores[i]
        
        nombre = diccionario['nombre']
        diccionario_datos[nombre] = diccionario
    
    return diccionario_datos

# Llamada a la función para leer el archivo CSV
nombre_archivo = 'datos.csv'
diccionario_datos = leer_csv(nombre_archivo)

# Imprimir el diccionario
print(diccionario_datos)
