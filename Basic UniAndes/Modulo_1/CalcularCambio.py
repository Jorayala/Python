Valor_Producto = float(input("Por favor introduzca el valor en pesos del producto que va a comprar:"))
Valor_Pagado = float(input("Por favor introduzca la cantidad de dinero en pesos con la que va a pagar:"))

cambio = Valor_Pagado - Valor_Producto


def calcular_cambio (cambio: float)-> str:
    A = cambio//500
    V1 = cambio%500
    B = V1//200
    V2 = V1%200
    C = V2//100
    V3 = V2%100
    D = V3//50


    return(A,B,C,D)


print("El numero de monedas es: ", calcular_cambio(cambio))