import matplotlib.pyplot as plt

# Datos para el gráfico
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Crear el gráfico de línea
plt.plot(x, y, marker='x', color='red', label='Línea')

# Agregar etiquetas y título
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico de Línea')

# Agregar leyenda
plt.legend()

# Mostrar el gráfico
plt.show()
