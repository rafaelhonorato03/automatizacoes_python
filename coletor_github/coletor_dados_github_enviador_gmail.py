from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import requests

reponse = requests.get(r"https://api.github.com./users/gabriel")
data = reponse.json()

#data


#Atribuição de variáveis
email = "rafael.honorato03@gmail.com"
senha = "@@"

destinatário = "rafael.honorato03@gmail.com"
assunto = "Informações recebidas via API GitHub"
mensagem = "Seguidores: %s\n Seguindo: %s\n" % (data["followers"], data["following"])

servico = Service(r"../recursos/chromedriver.exe")
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

password = driver.find_element(By.NAME,"password")
password.clear()
password.send_keys(senha)
password.send_keys(Keys.RETURN)
time.sleep(6)
print("Login realizado com sucesso!\n")

print("Abrindo caixa de e-mail...\n")
driver.get("https://mail.google.com/mail/u/0/#inbox")
time.sleep(2)

para = driver.find_element(By.NAME, "to")
para.send_keys(destinatário)
para.send_keys(Keys.RETURN)

titulo = driver.find_element(By.NAME, "subjectbox")
titulo.send_keys(assunto)
titulo.send_keys(Keys.RETURN)

corpo_de_texto = driver.find_element(By.XPATH, "//div[@role='textbox']")
corpo_de_texto.send_keys(mensagem)

enviar = driver.find_element(By.XPATH, "//div[@aria-label='Enviar (Ctrl-Enter)']")
enviar.click()
time.sleep(2)

driver.close()