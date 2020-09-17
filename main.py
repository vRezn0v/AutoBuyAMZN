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
cardDetails = CONFIG.get('ORDER', 'CARD')

url = CONFIG.get('ORDER', 'URL')
product_name = CONFIG.get('ORDER', 'PRODUCT')
product_asin = CONFIG.get('ORDER', 'ASIN')

driver = webdriver.Chrome(driver_path)
driver.maximize_window()
driver.get(url)

def openLoginPage():
    print("Logging In..")
    driver.find_element_by_id("nav-link-accountList").click()
    print('Login Button Clicked Successfully')
    

def submitLoginDetails():
    time.sleep(1)
    email_inp = driver.find_element_by_id("ap_email")
    email_inp.clear()
    email_inp.send_keys(user_email)
    driver.find_element_by_id("continue").click()
    time.sleep(0.5)
    driver.find_element_by_class_name("a-checkbox-label").click()
    pass_inp = driver.find_element_by_id("ap_password")
    pass_inp.clear()
    pass_inp.send_keys(user_pass)
    driver.find_element_by_id("signInSubmit").click()

def findProduct():
    searchbox = driver.find_element_by_id("twotabsearchtextbox")
    searchbox.clear()
    searchbox.send_keys(product_name)
    searchbox.send_keys(Keys.RETURN)
    product = driver.find_element_by_partial_link_text(product_name)
    print(product)
    product.click()

def initiatePurchase():
    button = driver.find_element_by_id("buy-now-button")
    button.click()

def makePayment():
    time.sleep(3)
    card = driver.find_element_by_xpath("//span[@data-number='" + cardDetails + "']")
    time.sleep(0.5)
    print("Yeet")
    card.click()
    cvv_input = driver.find_element_by_xpath("//input[@type='password' and @class='a-input-text a-form-normal a-width-small a-form-error']")
    cvv_input.send_keys(cvv)
    pay_button = driver.find_element_by_xpath("//input[@class='a-button-input a-button-text' and @type='submit' and @name='ppw-widgetEvent:SetPaymentPlanSelectContinueEvent']")
    pay_button.click()
    time.sleep(10)
    finalbtn = driver.find_element_by_name("placeYourOrder1")
    finalbtn.click()

def run():
    openLoginPage()
    time.sleep(0.5)
    submitLoginDetails()
    time.sleep(0.2)
    initiatePurchase()
    time.sleep(5)
    makePayment()
    print('\007')

run()