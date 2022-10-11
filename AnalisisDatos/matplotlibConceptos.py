from re import X
from tkinter import Y
import matplotlib.pyplot as plt
import matplotlib.patheffects as pa
import pandas as pd
# Comprobación que matplotlib funciona:
xi = [0,1,2,3,4,5,6]
yi = [0,1,4,9,16,25,36]

# plt.plot(xi,yi)
# plt.show()


# Conexion con csv
archivo = pd.read_csv(r'AnalisisDatos\EjemplosCSV\EstadisticasTotales.csv')

# Analizar todos los centrocampistas con mas de 7 goles:
centro = archivo[(archivo.posicion != 'Delantero') & (archivo.goles >= 5)]
centroClub = centro.club.value_counts()

# imprimir datos de forma predeterminada:
centroClub.plot(path_effects = [pa.SimpleLineShadow(),pa.Normal()])
centroClub.plot(color ='green', figsize = (10,5)) # Figsize para cambiar el tamaño de la grafica

# Imprimir con barras:
centroClub.plot(kind = 'bar', color = 'orange') # Con el color cambiamos el predeterminado
    # Imprimir de forma horizontal:
centroClub.plot(kind = 'barh')

# Imprimir con puntos
centro.plot(kind = 'scatter',x = 'nombre', y = 'goles')
 
 # Imprimir una tortilla:
centroClub.plot(kind = 'pie')

plt.show()



# Preparación de datos:
# Darle efectos:
centroClub.plot(linestyle = "-.", path_effects = [pa.SimpleLineShadow(),pa.Normal()])

# Añadir titulo a la x:
centroClub.set_xlabel("Equipos")
 # Añadiendo el plot a otras variables se Juntaran mas datos

 # Matplotlib sin pandas

plt.title("Titulo")
plt.xlabel("Titulo x")
plt.ylabel("Titulo y")
x = (4,8,13,17,20)
y = (54, 67, 98, 78, 45)

plt.scatter(x,y)
x = [2,4,6,7,9,13,19,26,29,31,36,40,48,51,57,67,69,71,78,88]
y = [54,72,43,2,8,98,109,5,35,28,48,83,94,84,73,11,464,75,200,54]
plt.scatter(x,y)
plt.show()

# Modificar el tamaño de los numeros referenciados en los ejes
plt.xticks(range(120, 180, 10))
plt.yticks(range(120, 180, 10))


# Juntar varios diagramas en una misma imagen:
"https://www.delftstack.com/es/howto/matplotlib/stack-bar-plots-matplotlib/"