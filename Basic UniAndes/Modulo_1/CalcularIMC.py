peso_lb = float(input("Por favor introduzca su peso en libras:"))
altura_inch = float(input("Por favor introduzca su altura en pulgadas:"))

peso_kl = peso_lb * 0.45359237
altura_mts = altura_inch * 0.0254

def calcular_BMI (peso_kl,altura_mts):
    imc = peso_kl/(altura_mts**2)
    return round(imc, 2)

print("El indice de masa coporal es: ", calcular_BMI(peso_kl,altura_mts))