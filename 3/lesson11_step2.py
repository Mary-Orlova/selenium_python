# Составные сообщения об ошибках и поиск подстроки
# Функция должна проверить вхождение строки substring в строку full_string
# с помощью оператора assert и, в случае несовпадения, предоставить исчерпывающее сообщение об ошибке.
# Тестируется через stdin -> stdout
# Пример отрицательный: input: fulltext some_value; Output: expected 'some_value' to be substring of 'fulltext';
# Пример положительный: input: 1 1; Output:

def test_substring(fulltext, some_value):
     assert some_value in fulltext, f"expected '{some_value}' to be substring of '{fulltext}'"

