import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Принять
    confirm = browser.switch_to.alert
    confirm.accept()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x = browser.find_element(By.ID, "input_value").text
    result = calc(x)


    # Заполняет поле значением Х по уникальному селектору
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(result)

    # Нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
