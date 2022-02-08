#Beatiful soup
#Instalamos librerias (Desde el terminal: pip install bs4 ) instalamos tambien (pip install requests)
#Instalamos pandas: pip install pandas
# Descargarmos desde el terminal pip install lxml (Con esto podemos leer paginas html) //No se usa porqu esta pandas
from itertools import count
from operator import eq
from bs4 import BeautifulSoup
import requests
import pandas as pd

#Ponemos el link de la pagina: #Vamos a obtener todos los equipos de la clasificación as
url = 'https://resultados.as.com/resultados/futbol/primera/clasificacion/'
page=requests.get(url) #Obtenemos la pagina
soup = BeautifulSoup(page.content, 'html.parser') #Para obtenerlos de una forma html
eq = soup.find_all('span',class_="nombre-equipo") #Obtenemos todos los valores de de la etiqueta span y clase nombre-equipo.
#Metemos los equipos en una lista
equipos = list()
count = 0
for i in eq:    
    if count == 20:
        break
    count +=1
    equipos.append(i.text) # Cogemos solo el texto de la etiqueta span

#Obtenemos los puntos
pt = soup.find_all('td',class_="destacado") #Obtenemos todos los valores de de la etiqueta span y clase nombre-equipo.
puntos = list()
count = 0
for i in pt:    
    if count == 20:
        break
    count +=1
    puntos.append(i.text) # Cogemos solo el texto de la etiqueta span
for i in range(0,20):
    print("posicion %d, equipo %s con %s puntos" % (i+1,equipos[i],puntos[i]))






















# ponemos el link de la pagina:
website = 'https://resultados.as.com/resultados/futbol/primera/clasificacion/'
result=requests.get(website) # Obtenemos la la pagina
content=result.text #Al resultado cogemos la parte tipo text.
soup = BeautifulSoup(content, 'lxml') # Escogemos el metodo de obtención del archivo html
# print(soup.prettify()) # hacemos un print de ello. prettify() sirve para que sea un poco más visual.
