from selenium import webdriver
import time
from faker import Faker

from selenium.webdriver.common.by import By


url = "https://suninjuly.github.io/file_input.html"
fake = Faker()


driver = webdriver.Chrome()

try:
    driver.maximize_window()
    driver.get(url)

    first_name = driver.find_element(By.NAME, "firstname")
    first_name.send_keys(fake.first_name())

    last_name = driver.find_element(By.NAME, "lastname")
    last_name.send_keys(fake.last_name())

    email = driver.find_element(By.NAME, "email")
    email.send_keys(fake.email())

    file = driver.find_element(By.NAME, "file")
    file.send_keys("C:/Users/nvzorov/environments/selenium_env/pythonProject3/shit.txt")
    # time.sleep(3)

    button_submit = driver.find_element(By.CSS_SELECTOR, "[type=submit]")
    button_submit.click()

    time.sleep(30)


except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
