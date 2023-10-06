def movimiento_robot(orientacion_actual, giro_1, giro_2, giro_3):
    
    # Función auxiliar para realizar el giro
    def giro(orientacion, comando):
        if orientacion == "N":
            if comando == "L":
                return "W"
            elif comando == "R":
                return "E"
            elif comando == "H":
                return "S"
            else:
                return "N"

        elif orientacion == "S":
            if comando == "L":
                return "E"
            elif comando == "R":
                return "W"
            elif comando == "H":
                return "N"
            else:
                return "S"

        elif orientacion == "E":
            if comando == "L":
                return "N"
            elif comando == "R":
                return "S"
            elif comando == "H":
                return "W"
            else:
                return "E"

        elif orientacion == "W":
            if comando == "L":
                return "S"
            elif comando == "R":
                return "N"
            elif comando == "H":
                return "E"
            else:
                return "W"

    # Aplicar los giros
    orientacion_actual = giro(orientacion_actual, giro_1)
    orientacion_actual = giro(orientacion_actual, giro_2)
    orientacion_actual = giro(orientacion_actual, giro_3)

    return orientacion_actual

# Ejemplo
orientacion_inicial = "N"
print(movimiento_robot(orientacion_inicial, "L", "R", "H"))  # Debería imprimir "S"
