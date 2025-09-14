import pytest
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGIN = "логин Степик"
PASSWORD = "пароль Степик"

urls = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
]


@pytest.mark.parametrize("url", urls)
def test_stepik_answer(url):
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)
    try:
        driver.get(url)

        # Авторизация
        wait.until(EC.presence_of_element_located((By.ID, "id_login_email"))).send_keys(LOGIN)
        driver.find_element(By.ID, "id_login_password").send_keys(PASSWORD)
        driver.find_element(By.CSS_SELECTOR, "button.sign-form__btn.button_with-loader").click()

        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".modal-signin")))

        # Дождаться появления поля для ответа и проверить, что оно пустое
        answer_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.smart-hints__hint")))
        assert answer_field.get_attribute("value") == "", "Поле для ответа должно быть пустым перед вводом"

        # Вычисление правильного ответа
        answer = str(math.log(int(time.time())))

        # Ввод ответа
        answer_field.send_keys(answer)

        # Нажать кнопку Отправить
        submit_button = driver.find_element(By.CSS_SELECTOR, "button.submit-submission")
        submit_button.click()

        # Ожидание фидбека и проверка текста
        feedback = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.smart-hints__hint_feedback")))

        # Проверка текста с осмысленным сообщением при ошибке
        assert feedback.text == "Correct!", f"Ожидался текст 'Correct!', но получен: '{feedback.text}'"

    finally:
        driver.quit()
