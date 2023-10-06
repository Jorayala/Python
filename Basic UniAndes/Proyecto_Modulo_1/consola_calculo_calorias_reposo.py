import calculadora_indices as ci

print("En esta funcion se va a calcular la cantidad de calorias que una persona quema estando en reposo")

peso = float(input("Por favor introduzca su peso en kilogramos:"))
altura = float(input("Por favor introduzca su altura en centimetros:"))
edad = float(input("Por favor introduzca su edad en anos:"))
valor_genero = float(input("Por favor introduzca el valor 5 en caso de ser hombre y el valor -161 en caso de ser mujer:"))
ccr = round(ci.calcular_calorias_en_reposo(peso, altura, edad, valor_genero), 2)

print(f"La cantidad de calorias que Usted quema en reposo son {ccr} cal ")