n = int(input("Ingrese el primer numero: "))
d = int(input("Ingrese el segundo numero: "))

def es_divisible (n: int , d:int)-> int:
    if d==0:
        r = 0
    if n%(2*d) == 0:
        r = 2
    elif n%d == 0:
        r = 1
    else:
        r = 0
    return r

print("El resultado es ", es_divisible(n,d))