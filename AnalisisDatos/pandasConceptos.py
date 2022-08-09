from sqlite3 import DatabaseError
import pandas as pd

# Conocer la version
# print(pd.__version__)

# Dataframes:

dataframe = pd.read_csv(r'AnalisisDatos\EjemplosCSV\dataframe.csv')
print(dataframe)


# Dataframe con acentos: 


# Para que salgan los acentos hay que abrir el archivo con un blog de notas y al guardar como cambiamos la codificación a utf-8
dataframe = pd.read_csv(r'AnalisisDatos\EjemplosCSV\dataframeutf8.csv')
# print(dataframe)

# Escribir columnas o series:
# print(dataframe.Nombre)
# print(dataframe["Edad"])
 # Escribir varias columnas:
print(dataframe[["Edad","Automovil"]])

