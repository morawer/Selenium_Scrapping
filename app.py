import time
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

    soup = BeautifulSoup(html, 'html.parser')

    span_elements = soup.find_all('span', id='lblLöpnummer')


# Iterar sobre los elementos <span> encontrados
    for span in span_elements:
    # Encontrar el elemento <a> dentro del <span>
        enlace = span.find('a')
    # Obtener el texto del elemento <a>
        texto = enlace.get_text()
    # Obtener el valor del atributo "href" del elemento <a>
        enlace_href = enlace['href']
    # Imprimir el resultado
        print("Texto del elemento: ", texto)
        print("Enlace del elemento: ", enlace_href)


 
if __name__ == "__main__":
    get_login()