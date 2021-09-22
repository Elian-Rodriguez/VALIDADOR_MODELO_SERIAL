#PROYECTO DE WEBSCRAPING PARA SACAR VIGENCIA DE GARANTIA Y MODELO ATRAVEZ DE UN ARCHIVO DE EXCEL COMO ENTRADA
#GENERANDO COMO SALIDA UN ARCHIVO TXT CON IDENTIFICADOR SERIAL MODELO Y MESES DE GARANTIA  PENDIENTES APARTIR DE LA FECHA.
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
import time
import pymysql
import pyautogui as pg
import time
import webbrowser as web
import os


miConexion = pymysql.connect( host='10.26.1.161', user= 'bart',port=3306, passwd='Linux-1234', db='TIENDAS' )
cur = miConexion.cursor()
consulta ="""select * from	TIENDAS.Tienda WHERE Estado != "ONLINE" AND Abierta = 1;"""
cur.execute(consulta)
datos = cur.fetchall()
valor = len(datos)
print(str(valor))
phone_no = "+57316 4158517"

mensaje ="LAS SIGUIENTES TIENDAS ESTAN FUERA DE LINEA:\n"
if valor > 0:
    for tienda in datos:
        mensaje =mensaje+tienda[2]+" - "+tienda[1]+"\n"
    parsedMessage =     mensaje
    web.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+parsedMessage)
    time.sleep(15)
    pg.write(' , ')
    pg.press('enter')
    print('Mensaje #'+' enviado')
    pass
    time.sleep(20)
    os.system("taskkill /im chrome.exe /f")
web