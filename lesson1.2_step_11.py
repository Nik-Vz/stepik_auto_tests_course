from selenium import webdriver
import time

from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.by import By


url = "https://suninjuly.github.io/text_input_task.html"

driver = webdriver.Chrome()

try:
    driver.maximize_window()
    driver.get(url=url)
    time.sleep(5)

    textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")
    textarea.send_keys("get()")
    time.sleep(5)

    submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")
    submit_button.click()
    time.sleep(5)

    try:
        # Переключаемся на всплывающее окно
        alert = driver.switch_to.alert
        # Получаем текст всплывающего окна и выводим его на экран
        print("Alert text:", alert.text)
        # Закрываем всплывающее окно (можно также принять его с помощью alert.accept())
        alert.dismiss()
    except UnexpectedAlertPresentException:
        # Если всплывающее окно было обработано другими средствами или неожиданно закрыто, обрабатываем исключение
        print("Unexpected alert was present but could not be handled")


except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
