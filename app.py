import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv

def get_login():
    # Get the variables from the .env file
    load_dotenv()
    user_login = os.getenv('USERLOGIN')
    password_login = os.getenv('PASSWORD')
    url_login = os.getenv('URL_LOGIN')

    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome()

    # Go to the login page
    driver.get(url_login)

    # Find the username and password fields
    username_input = driver.find_element(By.ID, "UserName")
    password_input = driver.find_element(By.ID, "Password")
    username_input.send_keys(user_login)
    password_input.send_keys(password_login)
    
    # Find the login button and click it
    login_button = driver.find_element(
        By.XPATH, "//button[contains(text(),'Iniciar sesión')]")
    login_button.click()
        
    html = driver.page_source  

    return html

def get_info(html):
    soup = BeautifulSoup(html, 'html.parser')
    spans = soup.find_all('tr')
    for span in spans:
        a = span.find('span', id='lblLöpnummer')
        span_tag = soup.find('span', {'id': 'lblLöpnummer'})


        # Encontrar la etiqueta "a" dentro de la etiqueta "span"
        a_tag = span_tag.find('a')

        # Obtener el valor del atributo "href"
        href = a_tag['href']

        # Obtener el texto contenido dentro de la etiqueta "a"
        texto = a_tag.get_text()

        # Imprimir los resultados
        print('href:', href)
        print('Texto:', texto)
    
 
 



 
if __name__ == "__main__":
    get_info(get_login())