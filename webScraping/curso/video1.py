from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

exe = 'C:\driversChrome\chromedriver.exe'
driver = webdriver.Chrome(executable_path=exe)
driver.get("https://gmail.com")
usuario = driver.find_element_by_id("identifierId")
usuario.send_keys("X@gmail.com") # Escribimos el usuario.
usuario.send_keys(Keys.ENTER) # Hacemos un enter
# driver.close()