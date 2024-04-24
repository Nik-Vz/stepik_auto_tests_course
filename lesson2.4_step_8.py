from selenium import webdriver
import time
from faker import Faker
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.common.by import By


import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


url = "https://suninjuly.github.io/explicit_wait2.html"
fake = Faker()


driver = webdriver.Chrome()
try:
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(url)

    # price = driver.find_element(By.CSS_SELECTOR, "#price")

    price = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element(
            (By.ID, "price"),
            "$100",
        )
    )

    book_button = driver.find_element(
        By.CSS_SELECTOR,
        "#book",
    )

    book_button.click()

    x = driver.find_element(By.CSS_SELECTOR, "#input_value")
    y = calc(int(x.text))

    answer = driver.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)

    submit_button = driver.find_element(By.CSS_SELECTOR, "#solve")
    submit_button.click()

    time.sleep(30)


except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
