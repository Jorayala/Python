import calculadora_indices as ci

print("En esta funcion se va a calcular el porcentaje de grasa")

peso = float(input("Por favor introduzca su peso en kilogramos:"))
altura = float(input("Por favor introduzca su altura en metros:"))
edad = float(input("Por favor introduzca su edad en anos:"))
valor_genero = float(input("Por favor introduzca el valor 10.8 en caso de ser hombre y el valor 0 en caso de ser mujer:"))
pgc = round(ci.calcular_porcentaje_grasa(peso, altura, edad, valor_genero), 2)

print(f"Su porcentaje de masa corporal es {pgc} %" )