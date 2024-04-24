from selenium import webdriver
import time
from faker import Faker
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.common.by import By


import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


url = "http://suninjuly.github.io/wait2.html"
fake = Faker()


driver = webdriver.Chrome()
try:
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(url)

    verify_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )

    verify_button.click()

    verify_text = driver.find_element(By.CSS_SELECTOR, "#verify_message").text
    assert "Verification was successful!" == verify_text
    time.sleep(3)


except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
