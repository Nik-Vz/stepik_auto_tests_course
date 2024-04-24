import random
from random import randrange

# import string
from faker import Faker


from selenium import webdriver
import time

from selenium.webdriver.common.by import By

# letters = string.ascii_lowercase

url = "http://suninjuly.github.io/huge_form.html"

driver = webdriver.Chrome()

try:
    driver.maximize_window()
    driver.get(url)
    text_fields = driver.find_elements(By.CSS_SELECTOR, "[type=text]")

    # for word in text_fields:
    #     word.send_keys("".join(random.choice(letters) for i in range(randrange(1, 10))))
    #     # time.sleep(0.5)

    for word in text_fields:
        fake = Faker()
        word.send_keys(fake.url())
        time.sleep(0.1)

    button_submit = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button_submit.click()

    # time.sleep(30)


except Exception as ex:
    print(ex)

finally:
    time.sleep(30)

    driver.close()
    driver.quit()
