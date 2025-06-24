from selenium import webdriver #serve para abrir navegador
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import xlrd

print("Iniciando o nosso Robô...\n")

#Criando um arquivo
arquivo = open("resultado_verificacao.txt","w")

dominios = []

#Lendo do excel
workbook = xlrd.open_workbook("lista_dominios.xls")
sheet = workbook.sheet_by_index(0)

for linha in range(0,20):
    dominios.append(sheet.cell_value(linha,0))

servico = Service(r"../recursos/chromedriver.exe")
driver = webdriver.Chrome(service=servico)
driver.get("https://registro.br/") #Entra no site
time.sleep(2)

for dominio in dominios:
    pesquisa = driver.find_element(By.ID,"is-avail-field")
    pesquisa.clear() #Limpando a barra de pesquisa
    pesquisa.send_keys(dominio)
    pesquisa.send_keys(Keys.RETURN)
    time.sleep(2)
    resultados = driver.find_elements(By.TAG_NAME,"strong")
    texto = ("Domínio %s %s" % (dominio, resultados[2].text))
    arquivo.write(texto + "\n")

arquivo.close()
time.sleep(2)
driver.quit()