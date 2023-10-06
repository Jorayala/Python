

def calcular_IMC (peso:float,altura:float)->float:
    imc = peso/(altura**2)
    return imc

def calcular_porcentaje_grasa (peso:float, altura:float, edad:int, valor_genero:float)-> float:
    
    gc = (1.2 * calcular_IMC (peso,altura)) + (0.23 * edad) - 5.4 - valor_genero

    return gc

def calcular_calorias_en_reposo  (peso:float, altura:float, edad:int, valor_genero:int)-> float:   
    tmb = (10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero
    return tmb

def calcular_calorias_en_actividad (peso:float, altura:float, edad:int, valor_genero:float, valor_actividad:float)-> float:  
    tmbaf = calcular_calorias_en_reposo  (peso, altura, edad, valor_genero) * valor_actividad
    return tmbaf

def consumo_calorias_recomendado_para_adelgazar (peso:float, altura:float, edad:int, valor_genero:float)-> str:

    XXX = round(0.8 * (calcular_calorias_en_reposo  (peso, altura, edad, valor_genero)), 2)
    ZZZ = round(0.85 * (calcular_calorias_en_reposo  (peso, altura, edad, valor_genero)), 2)
    return f"Para adelgazar es recomendado que consumas entre: {XXX} y  {ZZZ} calorías al día."

