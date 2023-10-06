import calculadora_indices as ci

print("En esta funcion se va a calcular la cantidad de calorias que una persona quema al realizar algun tipo de actividad fisica")

peso = float(input("Por favor introduzca su peso en kilogramos:"))
altura = float(input("Por favor introduzca su altura en centimetros:"))
edad = int(input("Por favor introduzca su edad en anos:"))
valor_genero = float(input("Por favor introduzca el valor 5 en caso de ser hombre y el valor -161 en caso de ser mujer:"))
valor_actividad = float(input("Por favor introduzca el valor correspondiente: /n 1.2 si hace poco o ningun ejercicio /n 1.375 si hacer ejercicio ligero /n 1.55 si hace ejercicio moderado /n 1.725 si es deportista /n 1.9 si es un atleta: "))
ccaf = round(ci.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad), 2)

print(f"La cantidad de calorias que Usted consume dependiendo de su actividad fisica es {ccaf} cal" )