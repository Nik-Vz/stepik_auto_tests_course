from selenium import webdriver
import time
from faker import Faker

from selenium.webdriver.common.by import By


import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


url = "https://suninjuly.github.io/wait1.html"
fake = Faker()


driver = webdriver.Chrome()
try:
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(url)

    verify_button = driver.find_element(By.CSS_SELECTOR, "#verify")
    verify_button.click()

    verify_text = driver.find_element(By.CSS_SELECTOR, "#verify_message").text
    assert "Verification was successful!" == verify_text
    time.sleep(3)


except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
