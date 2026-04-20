address_rows = [
    "  г. Омск; ул. Маркса, д. 3",
    "г.Томск,ул.Фрунзе,д.18  ",
    " г. Уфа , ул. Ленина; д.25 ",
]

# Список для хранения адресов после приведения к единому формату
clean_rows = []

for row in address_rows:
    # Убираем лишние пробелы и приводим разделители к общему виду
    normalized = row.strip()
    normalized = normalized.replace(";", ",")
    normalized = normalized.replace(", ", ",")
    normalized = normalized.replace(" ,", ",")
    # Добавляем пробелы после основных сокращений адреса
    normalized = normalized.replace("г.", "г. ")
    normalized = normalized.replace("ул.", "ул. ")
    normalized = normalized.replace("д.", "д. ")

    # Удаляем повторяющиеся пробелы внутри строки
    while "  " in normalized:
        normalized = normalized.replace("  ", " ")

    # Устанавливаем единый формат: после запятой один пробел
    normalized = normalized.replace(",", ", ")

    while "  " in normalized:
        normalized = normalized.replace("  ", " ")

    clean_rows.append(normalized.strip())

# Сравниваем исходные адреса и результат очистки
print("=== СРАВНЕНИЕ ===")

for row_index, row in enumerate(address_rows, start=1):
    print(f"#{row_index}")
    print(f"ДО: '{row}'")
    print(f"ПОСЛЕ: '{clean_rows[row_index - 1]}'")
    print()

# Почему выбраны такие адреса:
# каждый пример содержит ошибки форматирования, которые исправляются тем же алгоритмом.
