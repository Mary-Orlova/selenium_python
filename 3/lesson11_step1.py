# Составные сообщения об ошибках
# Тестируется через stdin -> stdout
# Пример отрицательный: expected 8, got 11; положительный: 11 11

def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"