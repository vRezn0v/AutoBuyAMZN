from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from configparser import ConfigParser



CONFIG = ConfigParser()
CONFIG.read('config.ini')

driver_path = CONFIG.get('MAIN', 'DRIVER_LOCATION')
user_email = CONFIG.get('CREDS', 'USERNAME')
user_pass = CONFIG.get('CREDS', 'PASSWORD')

cvv = CONFIG.get('ORDER', 'CVV') 

url = CONFIG.get('ORDER', 'URL')
product_name = CONFIG.get('ORDER', 'PRODUCT')

driver = webdriver.Chrome(driver_path)
driver.maximize_window()
driver.get(url)

def openLoginPage():
    print("Logging In..")
    driver.find_element_by_id("nav-link-accountList").click()
    print('Login Button Clicked Successfully')
    

def submitLoginDetails():
    email_inp = driver.find_element_by_id("ap_email")
    email_inp.clear()
    email_inp.send_keys(user_email)
    driver.find_element_by_id("continue").click()
    time.sleep(0.5)
    pass_inp = driver.find_element_by_id("ap_password")
    pass_inp.clear()
    pass_inp.send_keys(user_pass)
    driver.find_element_by_id("signInSubmit").click()

def findProduct():
    searchbox = driver.find_element_by_id("twotabsearchtextbox")
    searchbox.clear()
    searchbox.send_keys(product_name)
    searchbox.send_keys(Keys.RETURN)

def run():
    openLoginPage()
    time.sleep(1)
    submitLoginDetails()
    time.sleep(0.2)
    findProduct()

run()