#PROYECTO DE WEBSCRAPING PARA SACAR VIGENCIA DE GARANTIA Y MODELO ATRAVEZ DE UN ARCHIVO DE EXCEL COMO ENTRADA
#GENERANDO COMO SALIDA UN ARCHIVO TXT CON IDENTIFICADOR SERIAL MODELO Y MESES DE GARANTIA  PENDIENTES APARTIR DE LA FECHA.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
import time




options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=r"C:\Users\jose.lara\Documents\GitHub\VALIDADOR_MODELO_SERIAL\chromedriver.exe",options=options)
driver.get("https://www.lenovo.com/co/es/pc-services")
time.sleep(5)


filesheet = "Archivo_prueba.xlsx"
wb = load_workbook(filesheet)
nombres = wb.get_sheet_by_name('Hoja1')

wb.close()
agregar="CODIGO NCR;CODIGO SAP;SERIAL;MODELO"
i = 33
for i in range(1,222):
    cod_ncr, nom_tienda, serial = nombres[f'A{i}:C{i}'][0]

    ser= serial.value
    ELEMENTO = driver.find_element_by_name("serialNumber")
    ELEMENTO.send_keys(ser+Keys.ENTER)

    time.sleep(10)

    model  = driver.find_element_by_xpath('/html/body/div[2]/section[2]/div[1]/div[2]/div[1]/h4').text
    mes_garantia = driver.find_element_by_xpath('/html/body/div[2]/section[2]/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div/div/p/span[2]').text
    archivo2 = open("EXPORTADO_INICIO_GARANTIA.TXT",'a')
    linea="\n"+str(i) + ";" + str(cod_ncr.value) + ";" + str(nom_tienda.value) +";" + str(serial.value) + ";" + (model) + ";" +mes_garantia
    agregar=agregar+linea+"\n"
    archivo2.write(linea)
    archivo2.close()

    print(str(i),";",str(cod_ncr.value),";", str(nom_tienda.value),";", str(serial.value),";", (model),";",mes_garantia)

    driver.get("https://www.lenovo.com/co/es/pc-services")

    time.sleep(5)

driver.quit()

archivo = open("EXPORTADO.TXT",'w')
archivo.write(agregar)
archivo.close()