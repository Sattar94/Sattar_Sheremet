# Исходный набор складских позиций
materials_list = ["Кирпич", "Пескоблок", "Известь", "Гравий", "Черепица"]

# Показываем исходный список и примеры работы с индексами
print("=== КАТАЛОГ МАТЕРИАЛОВ ===")
print(f"Исходный список: {materials_list}")
print(f"Первый материал: {materials_list[0]}")
print(f"Последний материал: {materials_list[-1]}")
print(f"Средние элементы: {materials_list[1:4]}")

# Добавляем ещё два материала
materials_list.append("Стекло")
materials_list.append("Фанера")

print()
print("После добавления двух материалов:")
print(materials_list)

# Удаляем второй элемент списка
removed_name = materials_list.pop(1)

# Печатаем результат после изменения списка
print()
print(f"Удалённый второй элемент: {removed_name}")
print(f"Итоговый список: {materials_list}")
print(f"Длина списка: {len(materials_list)}")
