def convertir_a_conjunto(numero):
    digitos = set()  # Crear un conjunto vacío para almacenar los dígitos
    
    while numero > 0:
        digito = numero % 10  # Obtener el último dígito del número
        digitos.add(digito)  # Agregar el dígito al conjunto
        numero //= 10  # Eliminar el último dígito del número
    
    return digitos

def mismos_digitos(a, b):
    digitos_a = convertir_a_conjunto(a)
    digitos_b = convertir_a_conjunto(b)
    
    return digitos_a == digitos_b

# Ejemplo de uso
numero1 = 998
numero2 = 89
resultado = mismos_digitos(numero1, numero2)
print(resultado)  # Esto imprimirá True
