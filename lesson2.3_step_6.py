from selenium import webdriver
import time
from faker import Faker

from selenium.webdriver.common.by import By


import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


url = "https://suninjuly.github.io/redirect_accept.html"
fake = Faker()


driver = webdriver.Chrome()
try:
    driver.maximize_window()
    driver.get(url)

    trollface_button = driver.find_element(
        By.CSS_SELECTOR, ".trollface.btn.btn-primary"
    )
    trollface_button.click()
    time.sleep(3)

    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)

    x_element = driver.find_element(By.CSS_SELECTOR, "#input_value")
    y = calc(x_element.text)

    answer_field = driver.find_element(By.CSS_SELECTOR, "#answer")
    answer_field.send_keys(y)

    submit_button = driver.find_element(By.TAG_NAME, "button")
    submit_button.location_once_scrolled_into_view
    submit_button.click()
    time.sleep(30)


except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
