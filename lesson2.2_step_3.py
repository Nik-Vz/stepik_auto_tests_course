from selenium import webdriver
import time
from faker import Faker

from selenium.webdriver.common.by import By


url = "http://suninjuly.github.io/selects1.html"
fake = Faker()


driver = webdriver.Chrome()
try:
    driver.maximize_window()
    driver.get(url)

    x_element = driver.find_element(By.CSS_SELECTOR, "#num1")
    y_element = driver.find_element(By.CSS_SELECTOR, "#num2")
    sum_x_y = int(x_element.text) + int(y_element.text)

    dropdown = driver.find_element(By.CSS_SELECTOR, "#dropdown")
    dropdown.click()

    current_sum = driver.find_element(By.CSS_SELECTOR, f"option[value='{sum_x_y}']")
    current_sum.click()

    submit_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    submit_button.click()

    time.sleep(30)


except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
