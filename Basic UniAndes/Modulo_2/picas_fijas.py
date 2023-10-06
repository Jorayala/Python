numero_secreto = 1263
numero_intento = 2178

def picas_y_fijas(numero_secreto, numero_intento):
    picas = 0
    fijas = 0

    # Funciones para extraer dígitos
    def digito(num, i):
        return (num // 10**i) % 10

    # Verificamos cada dígito del numero_intento
    for i in range(4):
        digito_intento = digito(numero_intento, i)
        digito_secreto = digito(numero_secreto, i)
        
        # Verificar fijas
        if digito_secreto == digito_intento:
            fijas += 1
        # Verificar picas
        elif digito_intento in [digito(numero_secreto, j) for j in range(4)]:
            picas += 1
    
    return {"picas": picas, "fijas": fijas}

#numero_secreto = 7890
#numero_intento = 1807

resultado = picas_y_fijas(numero_secreto, numero_intento)
print(resultado)
