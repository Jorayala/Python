import math

S1 = float(input("Por favor introduzca la longitud del primer lado del triangulo:"))
S2 = float(input("Por favor introduzca la longitud del segundo lado del triangulo:"))
S3 = float(input("Por favor introduzca la longitud del tercer lado del triangulo:"))

def subperimetro (S1,S2,S3):
    s = (S1+S2+S3)/2
    return s

def area ():
    s = subperimetro (S1,S2,S3)
    area = math.sqrt(s*(s-S1)*(s-S2)*(s-S3))
    areaR = round(area, 1)
    return areaR

print("el area del triangulo es ", area())

