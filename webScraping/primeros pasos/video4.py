from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import time

website = 'https://es-es.facebook.com/'
path = 'C:\driversChrome\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get(website)
time.sleep(5)
# Aceptar cookies
galletas = driver.find_element_by_xpath('//*[@id="u_0_j_TX"]')
galletas.click()
