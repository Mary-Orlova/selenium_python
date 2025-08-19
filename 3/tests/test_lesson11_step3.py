from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class TestRegistration1(unittest.TestCase):
    def setUp(self):
        # Инициализация браузера
        self.browser = webdriver.Chrome()

    def test_registration1(self):
        self.browser.get("http://suninjuly.github.io/registration1.html")

        input1 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        input1.send_keys("Ivan")  # Ввод имени
        input2 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        input2.send_keys("Petrov")  # Ввод фамилии
        input3 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        input3.send_keys("test@ya.ru")  # Ввод email

        # Нажатие кнопки отправки формы
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Ожидание загрузки страницы с результатом
        time.sleep(1)

        # Нахождение элемента с текстом подтверждения регистрации
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        # Проверка -  текст подтверждения соответствует ожидаемому
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def tearDown(self):
        # Ожидание пару секунд, чтобы можно было визуально оценить результат
        time.sleep(2)
        # Закрытие браузера
        self.browser.quit()


class TestRegistration2(unittest.TestCase):
    def setUp(self):
        # Инициализация браузера
        self.browser = webdriver.Chrome()

    def test_registration2(self):
        self.browser.get("http://suninjuly.github.io/registration2.html")

        input1 = self.browser.find_element(By.CSS_SELECTOR, ".first_class .first")
        input1.send_keys("Ivan")  # Ввод имени
        input2 = self.browser.find_element(By.CSS_SELECTOR, ".third_class .third")
        input2.send_keys("test@ya.ru")  # Ввод email

        # Нажатие кнопки отправки формы
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Ожидание загрузки страницы с результатом
        time.sleep(1)

        # Нахождение элемента с текстом подтверждения регистрации
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        # Проверка - текст подтверждения соответствует ожидаемому
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def tearDown(self):
        # Ожидание пару секунд, чтобы можно было визуально оценить результат
        time.sleep(2)
        # Закрытие браузера
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
