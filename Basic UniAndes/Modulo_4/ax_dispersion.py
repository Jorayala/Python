import matplotlib.pyplot as plt

# Datos para la gráfica
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Crear una figura y un eje
fig, ax = plt.subplots()

# Dibujar la gráfica de dispersión (scatter plot)
ax.scatter(x, y, label='Puntos de datos', color='blue', marker='o')

# Agregar etiquetas y título
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_title('Gráfica de dispersión')

# Agregar una leyenda
ax.legend()

# Mostrar la gráfica
plt.show()
