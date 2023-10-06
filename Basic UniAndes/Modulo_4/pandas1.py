import pandas as pd
import math

# Leer el archivo CSV
data = pd.read_csv('wifi_gratis.csv', encoding='latin-1')

# Mostrar la información original
# print("Información original:")
# print(data)

#comuna90 = data[(data['COMUNA'] == "08") & (data["LATITUD"] == 6.236877)]
comuna90 = data[(data['COMUNA'] == "08")]
print(comuna90)
tipo = data.dtypes
print(tipo)
# # Filtrar y mostrar solo la información numérica
# info_numerica = data.select_dtypes(include=['number'])
# print("\nInformación numérica:")
# print(info_numerica)

# # Filtrar y mostrar solo la información no numérica
# info_no_numerica = data.select_dtypes(exclude=['number'])
# print("\nInformación no numérica:")
# print(info_no_numerica)
