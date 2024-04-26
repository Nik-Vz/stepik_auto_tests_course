from selenium import webdriver
from selenium.webdriver.common.by import By

import time


# options = ...
driver = webdriver.Chrome()
url = "https://suninjuly.github.io/find_link_text"

try:
    driver.maximize_window()
    driver.get(url)
    first_name = driver.find_element(By.NAME, "first_name")
    first_name.send_keys("Ivan")

    last_name = driver.find_element(By.NAME, "last_name")
    last_name.send_keys("Petrov")

    city = driver.find_element(By.CSS_SELECTOR, "input.form-control.city")
    city.send_keys("Smolensk")

    country = driver.find_element(By.ID, "country")
    country.send_keys("Russia")

    submit_button = driver.find_element(By.ID, "submit_button")
    submit_button.click()
    time.sleep(30)

except Exception as ex:
    print(ex)
finally:
    # driver.close()
    driver.quit()
