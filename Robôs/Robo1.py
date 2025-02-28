from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

print("Iniciando o nosso Robô...\n")

servico = Service(r"C:\Users\tabat\Documents\GitHub\automatizacoes_python\Robôs\chromedriver.exe")
driver = webdriver.Chrome(service=servico)

driver.get("https://registro.br/")
time.sleep(2) #dormindo
driver.close()