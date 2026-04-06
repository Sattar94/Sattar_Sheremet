# Температура в Цельсиях
celsius_value = 100

# Преобразуем её в шкалу Фаренгейта
fahrenheit_value = celsius_value * 9 / 5 + 32

# По температуре определяем агрегатное состояние воды
if celsius_value <= 0:
    state_name = "Лёд"
elif celsius_value >= 100:
    state_name = "Пар"
else:
    state_name = "Жидкость"

# Показываем результаты перевода температуры и определённого состояния воды
print("=== КОНВЕРТЕР ТЕМПЕРАТУР ===")
print(f"Температура в Цельсиях: {celsius_value} °C")
print(f"Температура в Фаренгейтах: {fahrenheit_value:.2f} °F")
print(f"Состояние воды: {state_name}")
