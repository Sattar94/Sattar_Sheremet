# Наборы материалов трёх бригад
team_1 = ["Кирпич", "Известь", "Гравий", "Стекло"]
team_2 = ["Известь", "Черепица", "Стекло", "Фанера"]
team_3 = ["Известь", "Стекло", "Гипсокартон", "Кирпич"]

# Получаем множества из исходных списков
group_1 = set(team_1)
group_2 = set(team_2)
group_3 = set(team_3)

# Ищем пересечения и различия
all_items = group_1 | group_2 | group_3
all_common = group_1 & group_2 & group_3
first_only = group_1 - group_2 - group_3
# Выделяем материалы, которые встречаются ровно у двух подрядчиков
for_two = (group_1 & group_2) | (group_1 & group_3) | (group_2 & group_3)
for_two = for_two - all_common

# Печатаем результаты сравнения множеств
print("=== АНАЛИЗ ЗАКАЗОВ ===")
print(f"Материалы первого подрядчика: {team_1}")
print(f"Материалы второго подрядчика: {team_2}")
print(f"Материалы третьего подрядчика: {team_3}")
print()
print(f"Все уникальные материалы: {sorted(all_items)}")
print(f"Общие для всех: {sorted(all_common)}")
print(f"Только у первого подрядчика: {sorted(first_only)}")
print(f"Ровно у двух подрядчиков: {sorted(for_two)}")
