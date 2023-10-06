def funcion(lista:list, x:int)-> int:
    resultado = 0
    i = len(lista) - 1
    while i < len(lista):
        resultado += lista[i]
        i -= 1
    return resultado
print(resultado)