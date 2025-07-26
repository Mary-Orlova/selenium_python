import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    img_x = browser.find_element(By.ID, "treasure")
    x_element = img_x.get_attribute("valuex")
    print("x_element=", x_element)
    x = x_element
    y = calc(x)


    # Заполняет поле значением Х по уникальному селектору
    answer= browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    # Проставление галочки по уникальному селектору I'm the robot
    robot = browser.find_element(By.ID, "robotCheckbox")
    robot.click()

    # Выбор в радио-баттен Robots rule
    robot_rule = browser.find_element(By.ID, "robotsRule")
    robot_rule.click()

    # Отправляет заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяет, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
