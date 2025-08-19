from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class TestRegistration(unittest.TestCase):
    def setUp(self):
        # Инициализация браузера перед каждым тестом
        self.browser = webdriver.Chrome()

    def fill_form_and_submit(self, link):
        # Открываем указанную страницу с формой регистрации
        self.browser.get(link)

        input1 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        input1.send_keys("Ivan")  # Ввод имени
        input2 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        input2.send_keys("Petrov")  # Ввод фамилии
        input3 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        input3.send_keys("test@ya.ru")  # Ввод email

        # Нажимаем кнопку отправки формы
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Ждем загрузки страницы с результатом
        time.sleep(1)

        # Возвращаем текст подтверждения регистрации
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        return welcome_text_elt.text

    def test_registration1(self):
        # Тест для первой версии формы регистрации
        welcome_text = self.fill_form_and_submit("http://suninjuly.github.io/registration1.html")
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_registration2(self):
        # Тест для второй версии формы регистрации
        welcome_text = self.fill_form_and_submit("http://suninjuly.github.io/registration2.html")
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def tearDown(self):
        # Ждем пару секунд, чтобы можно было визуально оценить результат
        time.sleep(2)
        # Закрываем браузер после каждого теста
        self.browser.quit()


if __name__ == "__main__":
    # Запуск всех тестов
    unittest.main()
