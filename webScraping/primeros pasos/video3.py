#https://www.youtube.com/watch?v=CHiwaFEUB1Y
from selenium import webdriver
import pandas as pd
from selenium.webdriver.support.ui import Select # Permite seleccionar valores dentro de una lista desplegable.
from selenium.webdriver.chrome.options import Options #Permite opciones a la hora de hacer la ejecucion.
import time
website = 'https://www.adamchoi.co.uk/teamgoals/detailed'
path = 'C:\driversChrome\chromedriver.exe'
opciones = Options()
opciones.add_argument("--headless") # Permite hacer el script en segundo plano.
driver = webdriver.Chrome(chrome_options=opciones, executable_path=path)
driver.get(website)
time.sleep(3)
#Aceptar cookies 
Cookiess = driver.find_element_by_xpath('/html/body/div[1]/div/a[1]')
Cookiess.click()
#Pulsar un boton.
all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
all_matches_button.click()


#Lista desplegable
lista = Select(driver.find_element_by_id('country')) # seleccionamos la lista desplegable
lista.select_by_visible_text('Spain') #Escogemos el valor visible
# lista despegable si no hubiera id
# caja = driver.find_element_by_class_name('panel-body')
# lista = Select(caja.find_element_by_id('country')) # seleccionamos la lista desplegable

time.sleep(3)
#Coger datos de la pagina.
partidos =  driver.find_elements_by_tag_name('tr')
datos = []
for partido in partidos:
    resultados = partido.text
    datos.append(resultados)

driver.quit() # Cerramos la conexión.

df = pd.DataFrame({'Partidos':datos})
print(df)
df.to_csv('Python\webScraping\csv\partidos.csv', index=False)