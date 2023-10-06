def picas_y_fijas(numero_secreto, numero_intento):
    picas = 0
    fijas = 0

    # Extraer dígitos del número secreto
    d1_secreto = numero_secreto % 10
    d2_secreto = (numero_secreto // 10) % 10
    d3_secreto = (numero_secreto // 100) % 10
    d4_secreto = numero_secreto // 1000

    # Extraer dígitos del número intento
    d1_intento = numero_intento % 10
    d2_intento = (numero_intento // 10) % 10
    d3_intento = (numero_intento // 100) % 10
    d4_intento = numero_intento // 1000

    # Comprobar fijas
    fijas += int(d1_secreto == d1_intento)
    fijas += int(d2_secreto == d2_intento)
    fijas += int(d3_secreto == d3_intento)
    fijas += int(d4_secreto == d4_intento)

    # Comprobar picas
    picas += int(d1_intento in [d1_secreto, d2_secreto, d3_secreto, d4_secreto]) - int(d1_secreto == d1_intento)
    picas += int(d2_intento in [d1_secreto, d2_secreto, d3_secreto, d4_secreto]) - int(d2_secreto == d2_intento)
    picas += int(d3_intento in [d1_secreto, d2_secreto, d3_secreto, d4_secreto]) - int(d3_secreto == d3_intento)
    picas += int(d4_intento in [d1_secreto, d2_secreto, d3_secreto, d4_secreto]) - int(d4_secreto == d4_intento)
    
    return {"picas": picas, "fijas": fijas}

numero_secreto = 1263
numero_intento = 2178

resultado = picas_y_fijas(numero_secreto, numero_intento)
print(resultado)
