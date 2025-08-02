import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()

    browser.get(link)

    # ждем загрузки страницы
    time.sleep(1)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )

    # Нажать на кнопку
    button2 = browser.find_element(By.ID, "book")
    button2.click()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x = browser.find_element(By.ID, "input_value").text
    result = calc(x)

    # Заполняет поле значением Х по уникальному селектору
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(result)

    # Нажать на кнопку
    button3 = browser.find_element(By.ID, "solve")
    button3.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
