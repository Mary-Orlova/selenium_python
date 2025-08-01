import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x = browser.find_element(By.ID, "input_value").text
    result = calc(x)


    # Заполняет поле значением Х по уникальному селектору
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(result)

    # Проставление галочки по уникальному селектору I'm the robot
    robot = browser.find_element(By.ID, "robotCheckbox")
    robot.click()

    # Отправляет заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")

    # Чтобы кликнуть на перекрытую кнопку,
    # В метод execute_script передали текст js-скрипта и найденный элемент button,
    # к которому нужно будет проскроллить страницу.
    # После выполнения кода элемент button должен оказаться в верхней части страницы.
    # button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    # Выбор в радио-баттен Robots rule
    robot_rule = browser.find_element(By.ID, "robotsRule")
    robot_rule.click()

    # Клик по кнопке отправки формы
    button.click()

    # Проверяет, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
