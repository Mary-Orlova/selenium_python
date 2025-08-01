from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


try:
    link = "https://suninjuly.github.io/selects1.html"
    # link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(num1, num2):
        summ = int(num1) + int(num2)
        return str(summ)

    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    summ = calc(num1, num2)

    # Заполняет поле значением summ
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(summ)

    # Отправляет заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
