# Размеры учебной аудитории
length_value = 8.4
width_value = 5.1
height_value = 3.2

# Цена покраски за квадратный метр
paint_cost_per_meter = 165

# Вычисляем площадь и объём помещения
floor_result = length_value * width_value
walls_result = 2 * (length_value + width_value) * height_value
volume_result = length_value * width_value * height_value

# Определяем цену окраски всех стен
painting_result = walls_result * paint_cost_per_meter

# Выводим все рассчитанные параметры помещения
print("=== ПАРАМЕТРЫ ПОМЕЩЕНИЯ ===")
print(f"Длина: {length_value} м")
print(f"Ширина: {width_value} м")
print(f"Высота: {height_value} м")
print()
print(f"Площадь пола: {floor_result:.2f} м²")
print(f"Площадь стен: {walls_result:.2f} м²")
print(f"Объём помещения: {volume_result:.2f} м³")
print(f"Стоимость покраски стен: {painting_result:.2f} руб.")
