from selenium import webdriver
import time
from faker import Faker

from selenium.webdriver.common.by import By


url = "https://suninjuly.github.io/find_xpath_form"
fake = Faker()


driver = webdriver.Chrome()

try:
    driver.maximize_window()
    driver.get(url)

    first_name = driver.find_element(By.NAME, "first_name")
    first_name.send_keys(fake.first_name())
    last_name = driver.find_element(By.NAME, "last_name")
    last_name.send_keys(fake.last_name())
    city = driver.find_element(By.CLASS_NAME, "city")
    city.send_keys(fake.city())
    country = driver.find_element(By.ID, "country")
    country.send_keys(fake.country())
    button_submit = driver.find_element(By.CSS_SELECTOR, "[type=submit]")
    button_submit.click()

    time.sleep(30)


except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
