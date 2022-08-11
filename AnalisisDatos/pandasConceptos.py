from sqlite3 import DatabaseError
import pandas as pd

# Conocer la version
# print(pd.__version__)

# Dataframes:

dataframe = pd.read_csv('AnalisisDatos\EjemplosCSV\dataframe.csv')
# print(dataframe)

# Mostrar todas las filas y columnas del dataframe
# pd.set_option('display.max_columns',None)# or 1000
# pd.set_option('display.max_rows',None)# or 1000
# pd.set_option('display.max_colwidth',-1)# or 199




# Dataframe con acentos: 


# Para que salgan los acentos hay que abrir el archivo con un blog de notas y al guardar como cambiamos la codificación a utf-8
dataframe = pd.read_csv('AnalisisDatos\EjemplosCSV\dataframeutf8.csv')
# print(dataframe)

# Escribir columnas o series:
# print(dataframe.Nombre)    
# print(dataframe["Edad"])
 # Escribir varias columnas:
# print(dataframe[["Edad","Automovil"]])


# READ_CSV:
dataframe = pd.read_csv('AnalisisDatos\EjemplosCSV\partidos.csv')
# print(csv)


# READ_EXCEL
try:
    excel = pd.read_csv("archivo.xlsx")
except:
    print("No se encuentra el archivo excel")


# Lecturas archivos json:
try:
    excel = pd.read_json("archivo.js")
except:
    print("No se encuentra el archivo json")

# Verificamos cuantas lineas y columnas tiene nuestro dataframe
# Filas y columnas:
print('\nFilas y columnas')
print(dataframe.shape)
# Filas
print('\nFilas')
print(dataframe.shape[0])
# Columnas
print('\nColumnas')
print(dataframe.shape[1])



# fILTRAR LOS PRIMEROS REGISTROS CON HEAD
print(dataframe.head())
# Imprimir los tres primeros registros
print(dataframe.head(3))

# Filtrar los ultimos registros:
print(dataframe.tail())
# Imprimir los tres ultimos registros
print(dataframe.tail(3))

# Comando info:
print(dataframe.info())

# Contemos registros repetidos de una columna:
print('\ntotal de partidos por jornada')
# print(dataframe.jornada.value_counts())
print(dataframe.jornada.value_counts(ascending=True,dropna=False)) # --> Ascending ordena valores, dropna elimina los nulos


# Ordenar registros:
# Dos formas: 
# --- Sirve para una columna
print(dataframe.goles_local.sort_values())

# --- Sirve para varias columnas:
print(dataframe.sort_values(by=['goles_local','jornada'],ascending=False).head())


# Filtrar por condiciones:
print(dataframe[dataframe.visitante == 'Arsenal'])
print(dataframe[(dataframe.visitante == 'Arsenal') & (dataframe.goles_local >=4)])
print(dataframe[(dataframe.visitante == 'Arsenal')| (dataframe.visitante == 'Leverkusen')& (dataframe.goles_local >=3)])


# Filtrar por str:
print(dataframe[dataframe.visitante.str.contains('Leverkusen')])
# Filtrar por la letra que empieza:
print(dataframe[(dataframe.visitante.str.startswith('B'))])

# Cambiamos el índice:
print(dataframe.set_index('jornada'))
###
jornadas=dataframe.set_index('jornada')
# Ordenar el indice:
print(jornadas.sort_index(ascending=True))
# Modificar para siempre la misma variable:
dataframe.set_index('jornada',inplace=True)
# resetearlo 
dataframe.reset_index(inplace=True)

# Filtrar por etiquetas:
# LOC SOLAMENTE FUNCIONA CON LOS INDICES
jornada = jornadas.loc[10]
# Si quiere usar una columna que no es indice:
arsenal = dataframe.loc[dataframe.visitante == 'Arsenal']


# Agrupar por indices de números enteros
print(dataframe.iloc[4])
print(dataframe.iloc[[4,2,5]])
print(dataframe.iloc[0:5])



# Group by
# agrupar:
agrupar_Jornada = dataframe.groupby('jornada')
# mostrar
print(list(agrupar_Jornada))
# Agrupar con for
for group_key, group_value in agrupar_Jornada:
    print(group_key)
    print(group_value)

# group by y sus funciones
print('\n\n\n\n\n\n\n\n\n\n\n')
# Agrupamos por equipos locales y su aforo y estudiamos la columna goles_local --> es el min max y total de veces
local=dataframe.groupby(['local','aforo']).agg({'goles_local' :['min', 'max','count']})
print(local)
# Usando esta version haría un max min y count de todas las columnas no agrupadas
# local=dataframe.groupby(['local','aforo']).agg(['min', 'max','count'])
# print(local)




