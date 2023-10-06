import calculadora_indices as ci

print("En esta funcion se va a calcular la cantidad de calorias que una persona debe consumir en caso desee adelgazar")

peso = float(input("Por favor introduzca su peso en kilogramos:"))
altura = float(input("Por favor introduzca su altura en centimetros:"))
edad = int(input("Por favor introduzca su edad en anos:"))
valor_genero = float(input("Por favor introduzca el valor 5 en caso de ser hombre y el valor -161 en caso de ser mujer:"))
ccra = (ci.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero))

print(ccra)