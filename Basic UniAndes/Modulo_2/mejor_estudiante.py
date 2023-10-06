def mejor_del_salon(est1, est2, est3, est4, est5):
    
    
    promedio1 = (est1["matematicas"] + est1["español"] + est1["ciencias"] + est1["literatura"] + est1["arte"]) / 5
    promedio2 = (est2["matematicas"] + est2["español"] + est2["ciencias"] + est2["literatura"] + est2["arte"]) / 5
    promedio3 = (est3["matematicas"] + est3["español"] + est3["ciencias"] + est3["literatura"] + est3["arte"]) / 5
    promedio4 = (est4["matematicas"] + est4["español"] + est4["ciencias"] + est4["literatura"] + est4["arte"]) / 5
    promedio5 = (est5["matematicas"] + est5["español"] + est5["ciencias"] + est5["literatura"] + est5["arte"]) / 5

    
    max_promedio = max(promedio1, promedio2, promedio3, promedio4, promedio5)
    mejores = []

    if promedio1 == max_promedio:
        mejores.append(est1["nombre"])
    if promedio2 == max_promedio:
        mejores.append(est2["nombre"])
    if promedio3 == max_promedio:
        mejores.append(est3["nombre"])
    if promedio4 == max_promedio:
        mejores.append(est4["nombre"])
    if promedio5 == max_promedio:
        mejores.append(est5["nombre"])
    
    
    return min(mejores).capitalize()


est1 = {"nombre": "Pedro", "matematicas": 5, "español": 5, "ciencias": 5, "literatura": 4, "arte": 5}
est2 = {"nombre": "Juan", "matematicas": 5, "español": 4.5, "ciencias": 4.2, "literatura": 4.5, "arte": 4.8}
est3 = {"nombre": "Ana", "matematicas": 5, "español": 4.5, "ciencias": 4.2, "literatura": 4.5, "arte": 4.8}
est4 = {"nombre": "Carlos", "matematicas": 4, "español": 3, "ciencias": 4, "literatura": 4, "arte": 3}
est5 = {"nombre": "Maria", "matematicas": 4.5, "español": 4.2, "ciencias": 4.1, "literatura": 4.8, "arte": 4.9}

print(mejor_del_salon(est1, est2, est3, est4, est5))
