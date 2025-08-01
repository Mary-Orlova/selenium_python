import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # ждем загрузки страницы
    time.sleep(1)

    # Нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Первое окно
    first_window = browser.window_handles[0]

    # Получаем массив имен вкладок
    new_window = browser.window_handles[1]
    # Переключаемся на нужную вкладку
    browser.switch_to.window(new_window)

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

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
