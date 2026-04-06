# Вводим номер дня по порядку
selected_day = int(input("Введите номер дня недели: "))

# Определяем название дня недели по введённому номеру
if selected_day == 1:
    day_title = "Понедельник"
elif selected_day == 2:
    day_title = "Вторник"
elif selected_day == 3:
    day_title = "Среда"
elif selected_day == 4:
    day_title = "Четверг"
elif selected_day == 5:
    day_title = "Пятница"
elif selected_day == 6:
    day_title = "Суббота"
elif selected_day == 7:
    day_title = "Воскресенье"
else:
    day_title = "Некорректный номер дня"

# Определяем рабочий режим для дня
if 1 <= selected_day <= 5:
    day_type = "Рабочий день"
    schedule_text = "8:00 - начало смены"
elif selected_day == 6 or selected_day == 7:
    day_type = "Выходной"
    schedule_text = "Отдых"
else:
    day_type = "Не определён"
    schedule_text = "Проверьте номер дня"

# Выводим итоговую информацию о выбранном дне
print("=== РАБОЧИЙ ГРАФИК ===")
print(f"Номер дня: {selected_day}")
print(f"День недели: {day_title}")
print(f"Тип дня: {day_type}")
print(f"Режим: {schedule_text}")
