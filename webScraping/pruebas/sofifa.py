from selenium import webdriver
import pandas as pd
from selenium.webdriver.support.ui import Select # Permite seleccionar valores dentro de una lista desplegable.
from selenium.webdriver.chrome.options import Options #Permite opciones a la hora de hacer la ejecucion.
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
def busquedajugadores(equipo):
    website = 'https://sofifa.com/teams'
    path = 'C:\driversChrome\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path)
    driver.get(website)
    Cookiess = driver.find_element(By.CLASS_NAME,'banner_continueBtn--3KNKl')
    Cookiess.click()
    time.sleep(2)
    Cookiess2 = driver.find_element(By.CLASS_NAME,'button_button--lgX0P.details_save--1ja7w')
    Cookiess2.click()
    Cookiess = driver.find_element(By.NAME,'keyword')
    Cookiess.send_keys(equipo)
    Cookiess.send_keys(Keys.ENTER)
    time.sleep(2)
    prueba = driver.find_element(By.XPATH,'//*[@id="body"]/div[1]/div/div[2]/div/table/tbody/tr/td[2]/a[1]/div')
    prueba.click()
    time.sleep(1)
    jugadores = driver.find_element(By.CLASS_NAME,'starting')
    nombre = jugadores.find_element(By.CLASS_NAME, 'col-name')
    nombre2 = nombre.find_element(By.CLASS_NAME, 'ellipsis')
    print(nombre2.text)

