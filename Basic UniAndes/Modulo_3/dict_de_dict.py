# Crear un diccionario de diccionarios
diccionario_principal = {
    "estudiante1": {
        "nombre": "Juan",
        "edad": 20,
        "cursos": ["Matemáticas", "Física"]
    },
    "estudiante2": {
        "nombre": "María",
        "edad": 22,
        "cursos": ["Biología", "Química"]
    },
    "estudiante3": {
        "nombre": "Pedro",
        "edad": 19,
        "cursos": ["Historia", "Literatura"]
    }
}
print(diccionario_principal)
# Acceder a la información en el diccionario de diccionarios
print(diccionario_principal["estudiante2"]["nombre"])  # Imprimirá "María"
print(diccionario_principal["estudiante1"]["cursos"][0])  # Imprimirá "Matemáticas"
