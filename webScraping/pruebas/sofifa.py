from lib2to3.pgen2 import driver
from selenium import webdriver
import pandas as pd
from selenium.webdriver.support.ui import Select # Permite seleccionar valores dentro de una lista desplegable.
from selenium.webdriver.chrome.options import Options #Permite opciones a la hora de hacer la ejecucion.
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import requests
def busquedajugadores(equipo):
    website = 'https://sofifa.com/teams'
    path = 'C:\driversChrome\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path)
    driver.get(website)
    #Aceptamos las cookies
    Cookiess = driver.find_element(By.CLASS_NAME,'banner_continueBtn--3KNKl')
    Cookiess.click()
    time.sleep(2)
    Cookiess2 = driver.find_element(By.CLASS_NAME,'button_button--lgX0P.details_save--1ja7w')
    Cookiess2.click()
    #Buscamos al equipo
    busquedaEquipo = driver.find_element(By.NAME,'keyword')
    busquedaEquipo.send_keys(equipo)
    busquedaEquipo.send_keys(Keys.ENTER)
    time.sleep(2)
    #Pinchamos en el equipo
    equipo = driver.find_element(By.XPATH,'//*[@id="body"]/div[1]/div/div[2]/div/table/tbody/tr/td[2]/a[1]/div')
    equipo.click()
    time.sleep(1)
    #Sacamos la url de la pagina de datos del equipo
    url_jugadores = driver.current_url
    listajugadores(url_jugadores)





def listajugadores(get_url):
    page = requests.get(get_url) # Optenemos la pagina
    soup = BeautifulSoup(page.content,'html.parser')
    lista = soup.find("tbody", class_="list")
    DiccJugadores = {}
    count = 0
    for a in lista.find_all("a"):
        if a.find("div", class_="ellipsis") == None: #Si un hijo del enlace no tiene una clase ellipsis se continua el for
            continue
        else:
            nombre_jugadores = a.find("div", class_="ellipsis")
            jugadores=(nombre_jugadores.text) # Cogemos solo el texto de la etiqueta span
            link = a.get('href') #Sacamos el link interno de la pagina
            DiccJugadores[jugadores]=link
            print(jugadores)
            sacardatosJugadores("https://sofifa.com"+link)
    # print(DiccJugadores)

def sacardatosJugadores(get_url):
    page = requests.get(get_url) # Optenemos la pagina
    soup = BeautifulSoup(page.content,'html.parser')
    datos = soup.find("div", class_="info")
    nombre = datos.find("h1")
    pais = datos.find("a")
    pais = pais.get("title")
    print("Pais:")
    print(pais)
    print("Nombre:")
    print(nombre.text)
    datosindi=datos.find("div")
    print("Datos:")
    print(datosindi.text)
    sacarvalor= soup.find("section", class_="card spacing")
    #Buscamos el valor entre las otras estadisticas:
    for i in sacarvalor.find_all("div", class_="block-quarter"):
        if i.find("div", class_="sub").text == "Value": #Si el texto del div es igual a value:
            valor = i.find("div").text
            valor=valor.replace("MValue","").replace("€","").replace("KValue","") #Eliminamos los datos no numericos del valor
    print(valor)


