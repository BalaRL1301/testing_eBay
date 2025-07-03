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
    print("DROPDOWN MENU TESTING STARTED")
    dropdown = driver.find_elenemt(By.XPATH, '//*[@id="gh"]/section/div/div/div/button')
    select = Select(dropdown)
    for i in range(1, 20):
        select.select_by_index(i)
        print(driver.title())