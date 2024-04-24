from selenium import webdriver
import time
from faker import Faker

from selenium.webdriver.common.by import By

# url для первой ссылки
# url = "https://suninjuly.github.io/registration1.html"

# url для второй ссылки
url = "https://suninjuly.github.io/registration2.html"

fake = Faker()


driver = webdriver.Chrome()
try:
    driver.maximize_window()
    driver.get(url)

    first_name = driver.find_element(
        By.CSS_SELECTOR,
        ".form-group.first_class input.form-control.first[placeholder='Input your first name']",
    )
    first_name.send_keys(fake.first_name())

    last_name = driver.find_element(
        By.CSS_SELECTOR, "[placeholder='Input your last name']"
    )
    last_name.send_keys(fake.last_name())

    email = driver.find_element(
        By.CSS_SELECTOR,
        "[placeholder='Input your email']",
    )
    email.send_keys(fake.email())

    button_submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button_submit.click()

    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

    time.sleep(5)

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
