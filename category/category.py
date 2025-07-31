from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import load_workbook
import time
import logging
import os
from selenium.webdriver.support.select import Select

def category_test(driver):
    print("DROPDOWN MENU(Left side) TESTING STARTED")
    dropdown = driver.find_elenemt(By.XPATH, '//*[@id="gh"]/section/div/div/div/button')
    select = Select(dropdown)
    for i in range(1, 20):
        select.select_by_index(i)
        #print(driver.title())
        driver.sleep(1)
        found = False # boolean for checking same item is redirected or not
        titles = driver.find_elements(By.CLASS_NAME, "s-item__title")
        for title in titles:
            title_text = title.text.strip().lower()
            if item.lower() in title_text:
                found = True
                #logging.info("listed", item)
                break
        if found:
            print("element found : " + driver.title())
        else:
            print("element not found : " + driver.title())
        driver.sleep(1)
    
    print("DROPDOWN MENU(left side) TESTING COMPLETED")
    drvier.refresh()
    driver.sleep(3)
    print("DROPDOWN MENU(right side) TESTING STARTED")
    droupdown1 = driver.find_element(By.XPATH, '//*[@id="gh-cat"]')
    select1 = Select(droupdown1)
    for j in range(1, 30):
        select1 .select_by_index(j)
        driver.spleep(1)
        found = 0
        titles = driver.find_elements(By.CLASS_NAME, "s-item__title")
        for t in titles:
            t_text = t.text.strip().lower()
            if item.lower() in t_text:
                found = 1
                break
        if found:
            print(driver.title() + "-> found")
        else:
            print(driver.title() + "-> not found")
        driver.sleep(1)

    print("DROPUDOWN MENU(right side) TESTING COMPLETED")
    driver.quit()