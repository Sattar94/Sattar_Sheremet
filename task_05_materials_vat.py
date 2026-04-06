# Цена единицы и количество в заказе
single_price = 180
units_count = 4

# Считаем стоимость до скидки
order_sum = single_price * units_count

# Выбираем уровень скидки по сумме
if order_sum < 1000:
    percent_discount = 0
elif order_sum <= 5000:
    percent_discount = 5
else:
    percent_discount = 10

# Подсчитываем скидку и итог к оплате
discount_sum = order_sum * percent_discount / 100
result_sum = order_sum - discount_sum

# Печатаем детали расчёта стоимости заказа
print("=== КАЛЬКУЛЯТОР СКИДКИ ===")
print(f"Цена за единицу: {single_price:.2f} руб.")
print(f"Количество товара: {units_count}")
print(f"Стоимость без скидки: {order_sum:.2f} руб.")
print(f"Размер скидки: {percent_discount}%")
print(f"Сумма скидки: {discount_sum:.2f} руб.")
print(f"Итоговая стоимость: {result_sum:.2f} руб.")

# Пример покупки:
# взято 4 товара по 180 рублей.
# ожидаемый вывод: скидка не будет применена
