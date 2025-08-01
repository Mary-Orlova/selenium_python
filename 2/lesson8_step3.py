from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняет обязательные поля по уникальному селектору
    name = browser.find_element(By.NAME, "firstname")
    name.send_keys("Ivan")
    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Petrov")
    mail = browser.find_element(By.NAME, "email")
    mail.send_keys("test@ya.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла

    file = browser.find_element(By.ID, "file")
    file.send_keys(file_path)

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
