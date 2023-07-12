import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime
import time
import urllib

# service = Service(
#     executable_path=r'./msedgedriver.exe',
#     service_log_path=os.devnull,
# )
options = webdriver.EdgeOptions()
options.add_argument('--disable-extensions')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')

# navegador = webdriver.Edge(service=service, options=options)
navegador = webdriver.Edge()
# navegador = webdriver.Edge(options=options)
navegador.get("https://web.whatsapp.com/")
time.sleep(20)
dia = datetime.now().day
mes = datetime.now().month
hora = datetime.now().hour
minuto = datetime.now().minute
numero = 558589474637
texto = urllib.parse.quote(f"Dia {dia}/{mes}: Saída {hora}h{minuto}")
link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
navegador.get(link)

# while len(navegador.find_element(By.ID, "side")) < 1:
#     time.sleep(20)
time.sleep(10)

navegador.find_element(By.XPATH, '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER)
time.sleep(20)

# navegador.quit()