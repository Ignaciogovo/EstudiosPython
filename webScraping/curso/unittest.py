from lib2to3.pgen2 import driver
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
exe = 'C:\driversChrome\chromedriver.exe'
class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=exe)

    def test_buscar(self):
        driver = self.driver
        driver.get('http://www.google.com')
        self.assertIn("google", driver.title) # buscamos el titulo google en el driver, para comprobar.
        elemento = driver.find_element_by_name("q")
        elemento.send_keys("selenium")
        elemento.send_keys(Keys.RETURN) # Return es como un enter
        time.sleep(4)
        assert "No se encontró el elemento" not in driver.page # Si no encuentra google en el driver, sale esta condicion

    def tearDown(self):
        self.driver.close()
