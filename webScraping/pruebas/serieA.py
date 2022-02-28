from bs4 import BeautifulSoup
import requests
import time
import sofifa
# link pagina:
url = "https://us.as.com/resultados/futbol/italia/clasificacion/"
page = requests.get(url) # Optenemos la pagina
soup = BeautifulSoup(page.content,'html.parser')
nombre_equipo = soup.find_all("span", class_="nombre-equipo")
equipos = list()
count = 0
for i in nombre_equipo:
    if count == 20:
        break
    count +=1
    equipo = i.text
    if equipo == "Nápoles":
        equipo = "Napoli"
    equipos.append(equipo) # Cogemos solo el texto de la etiqueta span
for i in range(0,2):
    print("puesto: %d equipo: %s" % (i+1, equipos[i]))
    sofifa.busquedajugadores(equipos[i])
