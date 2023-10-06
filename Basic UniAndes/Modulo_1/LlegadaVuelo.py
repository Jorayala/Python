hora_salida = int(input("Introduce la hora de inicio (0-23): "))
minuto_salida = int(input("Introduce los minutos de inicio (0-59): "))
segundo_salida = int(input("Introduce los segundos de inicio (0-59): "))

duracion_horas = int(input("Introduce la duración en horas: "))
duracion_minutos = int(input("Introduce la duración en minutos: "))
duracion_segundos = int(input("Introduce la duración en segundos: "))



def calcular_horario_llegada(hora_salida, minuto_salida, segundo_salida, duracion_horas, duracion_minutos, duracion_segundos):

    # Sumar Segundos
    segundos_llegada = segundo_salida + duracion_segundos
    llevar_minutos = segundos_llegada//60
    segundos_llegada %= 60

    minutos_llegada = minuto_salida + duracion_minutos + llevar_minutos
    llevar_horas = minutos_llegada//60
    minutos_llegada %=60

    horas_llegada = hora_salida + duracion_horas + llevar_horas
    horas_llegada %=24

    return(horas_llegada, minutos_llegada, segundos_llegada)

print("la hora de llegada sera : ", calcular_horario_llegada(hora_salida, minuto_salida, segundo_salida, duracion_horas, duracion_minutos, duracion_segundos))



