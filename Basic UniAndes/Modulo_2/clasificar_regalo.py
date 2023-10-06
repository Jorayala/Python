id = int(input("Por favor ingrese el numero id del regalo [100-999]: "))

def clasificar_regalo (id:int)-> str:
    id_str = str(id)
    if id_str[0]==id_str[2] and id%2 != 0:
        respuesta = "girl"
    elif  id_str[0]==id_str[2] and id%2 == 0:   
        respuesta = "boy"
    elif  id_str[0]!=id_str[2] and id%2 == 0:   
        respuesta = "man"   
    else:
        respuesta = "woman"
    return respuesta

print("El numero ingresado corresponde a", clasificar_regalo(id))






