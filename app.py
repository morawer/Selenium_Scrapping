from selenium import webdriver
from selenium.webdriver.common.by import By
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
    
get_login()