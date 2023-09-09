from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")

drivers = []
ids = []
filas = []
testes1 = []
testes2 = []

i = 0
while True:
    driver = webdriver.Chrome(options=chrome_options)
    drivers.append(driver)

    print("Acessando site da T4F - Navegador {}".format(i))
    driver.get("https://taylor-swift-sp.sales.ticketsforfun.com.br/")
    print('Site da T4F acessado')
    time.sleep(20)

    id = driver.find_element(By.ID, "hlLinkToQueueTicket2")
    print(id.text)
    ids.append(id.text)
    
    nome_arquivo = "resultados.txt"
    
    with open(nome_arquivo, "a", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([])

    print('\n')
    i += 1
