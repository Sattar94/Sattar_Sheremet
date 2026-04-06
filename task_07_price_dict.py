# Словарь материалов с ценами
materials_costs = {
    "Кирпич": 28.0,
    "Пескоблок": 52.0,
    "Известь": 260.0,
    "Гравий": 980.0,
    "Черепица": 1450.0,
}

print("=== ПРАЙС-ЛИСТ МАТЕРИАЛОВ ===")
print(f"Исходный словарь: {materials_costs}")

# Добавляем в прайс новые строки
materials_costs["Стекло"] = 890.0
materials_costs["Фанера"] = 1200.0

print()
print("После добавления двух материалов:")
print(materials_costs)

# Повышаем цену извести на 10%
materials_costs["Известь"] = materials_costs["Известь"] * 1.10

# Подготавливаем словарь для аккуратного отображения цен
formatted_costs = {name: f"{price:.2f}" for name, price in materials_costs.items()}

print()
print("После изменения цены извести на 10%:")
print(formatted_costs)

# Удаляем один материал из словаря
deleted_price = materials_costs.pop("Гравий")
formatted_costs = {name: f"{price:.2f}" for name, price in materials_costs.items()}

print()
print(f"Удалённый материал: Гравий ({deleted_price:.2f} руб.)")
print(f"Итоговый словарь: {formatted_costs}")

# Вычисляем среднее значение цены
mean_price = sum(materials_costs.values()) / len(materials_costs)

# Выводим среднюю цену по всем материалам, оставшимся в словаре
print(f"Средняя цена материалов: {mean_price:.2f} руб.")
