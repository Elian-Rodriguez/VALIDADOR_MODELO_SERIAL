#192.168.1.222
#PROYECTO DE WEBSCRAPING PARA SACAR VIGENCIA DE GARANTIA Y MODELO ATRAVEZ DE UN ARCHIVO DE EXCEL COMO ENTRADA
#GENERANDO COMO SALIDA UN ARCHIVO TXT CON IDENTIFICADOR SERIAL MODELO Y MESES DE GARANTIA  PENDIENTES APARTIR DE LA FECHA.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
import time
from selenium.webdriver.support.ui import Select
#from Selenium.common.exceptions import NoSuchElementException


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=r"C:\Users\jose.lara\Documents\GitHub\VALIDADOR_MODELO_SERIAL\chromedriver.exe",options=options)
driver.get("http://192.168.1.222/cgi-bin/luci/;stok=01a427880dd387f07939c50ff3537c6f/admin/configuration/")
time.sleep(5)
USSER = driver.find_element_by_id("cbi-input-user")
CLAVE = driver.find_element_by_id("cbi-input-password")
user ="admin"
USSER.send_keys(user)
CLAVE.send_keys(user+Keys.ENTER)

continue_link = driver.find_element_by_partial_link_text('Configuration')
continue_link.click()

select = Select(driver.find_element_by_id('cbi-network-general-internet_connection_type'))

continue_link = driver.find_element_by_id('')

continue_link.click()



time.sleep(3)



#/html/body/div[2]/div[5]/div/form/div[1]/div/div

#cbi-input-user
#cbi-input-password