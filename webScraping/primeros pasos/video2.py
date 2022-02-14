# https://youtu.be/0AvX54Rp4sc
#Librerias
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait # Permite esperar que carguen los elementos de la pagina
from selenium.webdriver.support import expected_conditions # Importamos la condicion esperada.
from selenium.webdriver.common.by import By # A traves de unos elementos del html
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# Opciones de navegación
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized') #Esto es para que se inice maximizado 
options.add_argument('--disable-extensions') # Desactivamos todas las posibles extensiones

driver_path = 'C:\driversChrome\chromedriver.exe'
driver = webdriver.Chrome(driver_path, chrome_options=options)

#Iniciamos el navegador
driver.get('https://eltiempo.es')
#Timeout de 5s, si no se ejecuta en 5 segundos,se detiene
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable(By.CSS_SELECTOR,
            'button.didomi-components-button didomi-button didomi-dismiss-button didomi-components-button--color didomi-button-highlight highlight-button'.replace(' ', '.')))\
            .click()
