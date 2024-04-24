from selenium import webdriver
import time
from faker import Faker

from selenium.webdriver.common.by import By

import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


url = "https://suninjuly.github.io/get_attribute.html"
fake = Faker()


driver = webdriver.Chrome()
try:
    driver.maximize_window()
    driver.get(url)

    x_element = driver.find_element(By.CSS_SELECTOR, "#treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    answer_field = driver.find_element(By.CSS_SELECTOR, "#answer")
    answer_field.send_keys(y)

    checkbox = driver.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    radiobutton = driver.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobutton.click()

    submit_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    submit_button.click()
    time.sleep(30)


except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
