# Автоматизация тестирования с помощью Selenium и Python

Выполнение практических заданий курса "Автоматизация тестирования с помощью Selenium и Python"

Проект демонстрирует ключевые навыки автоматизации веб-тестирования: от базовых поисков элементов до сложных сценариев с Page Object Model.

**Изученные технологии и приёмы:**

- Selenium: find_element/find_elements, работа с radio buttons, checkboxes, dropdowns, загрузка файлов, переключение вкладок, ожидания

- Решение капч для роботов

- Тестирование форм

- unittest и pytest (маркировка, параметризация, pytest-rerunfailures)

- Page Object Model


---
# Финальная часть проекта 

---
**Используемые технологии:**
- Python==3.9.9 
- PySocks==1.7.1
- pytest==8.4.1
- pytest-rerunfailures==16.0.1
- selenium==4.34.2
- trio-websocket==0.12.2
- websocket-client==1.8.0

---
**Структура проекта:**
- pages/ — папка со страницами:

  - base_page — базовый класс страницы

  - basket_page — страница корзины

  - locators — локаторы элементов

  - login_page — страница логина/регистрации

  - main_page — главная страница

  - product_page — страница продукта

**В корне проекта:**
- pytest.ini - конфигурация pytest
- requirements.txt - зависимости

---
**Установка и запуск**:
1. Клонировать репозиторий: 
```
git clone git@github.com:Mary-Orlova/selenium_python.git
```

2. Создать виртуальное окружение
```
python -m venv venv
```

3. Активировать виртуальное окружение
- для macOS/Linux:
``
source venv/bin/activate
``
- для Windows: 
``
.\venv/Scripts/activate
``

4. Установить зависимости
```
pip install -r requirements.txt
```
5. Запуск тестов с маркером need_review из корня проекта
```
pytest -v 4/4_3_7 --browser_name=chrome --tb=line --language=en -m need_review
```

6. Вы великолепны! 