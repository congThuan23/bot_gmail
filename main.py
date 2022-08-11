# -*- coding: utf-8 -*-

import csv
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

path = './asstes/chromedriver.exe'
url = 'https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp'

with open('./asstes/info_user.csv','r') as csv_file:
    
    csv_reader = csv.reader(csv_file)
    
    for line in csv_reader:
        
        driver = webdriver.Chrome(executable_path=path)
        driver.get(url)
        time.sleep(3)

        lastname_field = driver.find_element_by_id('lastName')
        lastname_field.send_keys(line[0])
        time.sleep(3)
        
        firstname_field = driver.find_element_by_id('firstName')
        firstname_field.send_keys(line[1])
        time.sleep(3)
        
        #try:
        username_field = driver.find_element_by_id('username')
        username_field.send_keys(line[2])
        time.sleep(3)

        password_field = driver.find_element_by_name('Passwd')
        password_field.send_keys(line[3])
        time.sleep(3)

        confirmPasswd_field = driver.find_element_by_name('ConfirmPasswd')
        confirmPasswd_field.send_keys(line[3])
        time.sleep(3)

        # click-------------------------------------------------------------
        goahead = driver.find_element_by_xpath('//*[@id="accountDetailsNext"]/div/button')
        goahead.click()       
        time.sleep(2)
        
        phonenumber_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#phoneNumberId")))
        phonenumber_field.send_keys(line[4])                                      
        
        goahead1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#view_container > div > div > div.pwWryf.bxPAYd > div > div.zQJV3 > div > div.qhFLie > div > div > button")))
        goahead1.click()
        time.sleep(3)
        
        otp = driver.find_element(by=By.XPATH, value='(//*[@class="whsOnd zHQkBf"])')
        otp.click()
        time.sleep(1)
        # maXM.send_keys()
        tg = 2
        # browser.implicitly_wait(tg)
        while len(otp.get_attribute('value')) != 6:
            driver.implicitly_wait(tg)
        time.sleep(10)
         
        # click-------------------------------------------------------------
        goahead2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#view_container > div > div > div.pwWryf.bxPAYd > div > div.zQJV3 > div.dG5hZc > div.qhFLie > div > div > button")))
        goahead2.click()
        time.sleep(3)      

        Bday_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#day")))
        Bday_field.send_keys(line[5])
        time.sleep(3)
        
        Mday_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#month")))
        Mday_field.send_keys(line[6])
        time.sleep(3)
        
        Yday_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#year")))
        Yday_field.send_keys(line[7])
        time.sleep(3)
        
        Gender_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#gender")))
        Gender_field.send_keys(line[8])
        time.sleep(3)

        goahead3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#view_container > div > div > div.pwWryf.bxPAYd > div > div.zQJV3 > div.dG5hZc > div.qhFLie > div > div > button")))
        goahead3.click()
        time.sleep(3)
        
        goahead4 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#view_container > div > div > div.pwWryf.bxPAYd > div > div.zQJV3 > div.dG5hZc > div.qhFLie > div > div > button")))
        goahead4.click()
        time.sleep(3)

        goahead5 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#view_container > div > div > div.pwWryf.bxPAYd > div > div.zQJV3 > div > div.qhFLie > div > div > button")))
        goahead5.click()
        time.sleep(3)
        break
    
