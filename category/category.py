from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def category_test():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.ebay.com/")
    print("DROPDOWN MENU (Right side) TESTING STARTED")

    try:
        for i in range(1, 35):
            wait.until(EC.presence_of_element_located((By.ID, "gh-cat")))
            dropdown = driver.find_element(By.ID, "gh-cat")
            select = Select(dropdown)
            category_name = select.options[i].text
            print(f"Selecting category: {category_name}")

            select.select_by_index(i)

            search_box = driver.find_element(By.ID, "gh-ac")
            search_box.clear()
            search_box.send_keys("\n")

            time.sleep(2)
            page_title = driver.title

            if category_name.lower() in page_title.lower():
                print("FOUND")
            else:
                print("NOT FOUND")

        print("DROPDOWN MENU (Right side) TESTING COMPLETED")

    except Exception as e:
        print("Right dropdown test failed:", str(e))

    driver.quit()