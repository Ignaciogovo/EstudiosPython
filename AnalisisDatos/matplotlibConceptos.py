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