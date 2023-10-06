import calculadora_indices as ci

print("En esta funcion se va a calcular el Indice de Masa Corporal (IMC)")

peso = float(input("Por favor introduzca su peso en kilogramos:"))
altura = float(input("Por favor introduzca su altura en metros:"))
imc = round(ci.calcular_IMC(peso, altura), 2)

print("Su indice de masa corporal es", imc )