from selenium import webdriver
import time
import math

from selenium.webdriver.common.by import By


url = "http://suninjuly.github.io/find_link_text"
x = str(math.ceil(math.pow(math.pi, math.e) * 10000))
print(x)


driver = webdriver.Chrome()

try:
    driver.maximize_window()
    driver.get(url)
    numbers = driver.find_element(By.PARTIAL_LINK_TEXT, "224592")
    numbers.click()
    time.sleep(1)

    first_name = driver.find_element(By.NAME, "first_name")
    first_name.send_keys("Ivan")
    last_name = driver.find_element(By.NAME, "last_name")
    last_name.send_keys("Petrov")
    city = driver.find_element(By.CLASS_NAME, "city")
    city.send_keys("Smolensk")
    country = driver.find_element(By.ID, "country")
    country.send_keys("Russia")
    button_submit = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button_submit.click()

    time.sleep(30)


except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
