import pandas as pd

# Crear una serie de Pandas con los números del 1 al 5
serie = pd.Series([1, 2, 3, 4, 5])
print(serie[0])
print(serie[0:1])
print(serie.loc[0])
print(serie.iloc[1])
# Imprimir la serie
print(serie)
