from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#Atribuição de variáveis
email = "rafael.honorato03@gmail.com"
senha = "@@"
destinatário = "rafael.honorato03@gmail.com"
assunto = "E-mail enviado pelo robô"
mensagem = "Primeiro e-mail enviado pelo nosso robô"

servico = Service(r"C:\Users\tabat\Documents\GitHub\automatizacoes_python\Robôs\chromedriver.exe")
driver = webdriver.Chrome(service=servico)

print("Iniciando o nosso Robô...\n")
print("Acessando o Gmail...\n")
driver.get("https://gmail.com.br/")

#LOGIN
print("Realizando login...\n")
login = driver.find_element(By.ID, "identifierId")
login.clear()
login.send_keys(email)
login.send_keys(Keys.RETURN)
time.sleep(2)

password = driver.find_element(By.NAME, "password")
password.clear()
password.send_keys(senha)
password.send_keys(Keys.RETURN)
time.sleep(6)
print("Login realizado com sucesso!\n")

driver.close()