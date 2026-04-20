warehouse_data = {
    "Кирпич": {"quantity": 3400, "price": 15.00, "min_quantity": 900},
    "Известь": {"quantity": 90, "price": 250.00, "min_quantity": 40},
    "Гравий": {"quantity": 6, "price": 950.00, "min_quantity": 12},
    "Стекло": {"quantity": 24, "price": 870.00, "min_quantity": 18},
    "Фанера": {"quantity": 11, "price": 1250.00, "min_quantity": 15},
}

# Печатаем шапку отчёта по складу
print("=" * 70)
print("СИСТЕМА УЧЁТА СКЛАДА")
print("=" * 70)
print()
print("Материал | Кол-во | Цена | Мин. | Стоимость")
print("-" * 70)

# Переменные для накопления общей статистики
full_total = 0
critical_list = []
expensive_name = ""
expensive_value = 0

for item_name, item_data in warehouse_data.items():
    # Получаем характеристики текущей позиции склада
    qty = item_data["quantity"]
    cost = item_data["price"]
    min_qty = item_data["min_quantity"]
    total_item_cost = qty * cost

    # Накапливаем общую стоимость всех остатков
    full_total += total_item_cost

    # Ищем материал с максимальной суммарной стоимостью на складе
    if total_item_cost > expensive_value:
        expensive_value = total_item_cost
        expensive_name = item_name

    # Помечаем материалы, остаток которых ниже минимального порога
    danger_mark = ""
    if qty < min_qty:
        danger_mark = "  CRITICAL"
        critical_list.append(f"{item_name}: {qty} < {min_qty}")

    print(
        f"{item_name} | {qty} | {cost:.2f} | "
        f"{min_qty} | {total_item_cost:.2f}{danger_mark}"
    )

print("=" * 70)
print(f"ОБЩАЯ СТОИМОСТЬ: {full_total:.2f} руб")
print(
    f"Самый дорогой: {expensive_name} "
    f"({expensive_value:.2f} руб)"
)
print()
print(f"КРИТИЧЕСКИЕ ОСТАТКИ ({len(critical_list)}):")

# Выводим список дефицитных позиций, если они обнаружены
if critical_list:
    for item_name in critical_list:
        print(f"- {item_name}")
else:
    print("Нет критических остатков")

print()
print("=== ВЫДАЧА МАТЕРИАЛА ===")

selected_material = "Известь"
selected_quantity = 15

# Проверяем наличие материала и возможность его выдачи со склада
if selected_material in warehouse_data:
    available_quantity = warehouse_data[selected_material]["quantity"]

    if available_quantity >= selected_quantity:
        warehouse_data[selected_material]["quantity"] -= selected_quantity
        print(f"Выдано {selected_quantity} единиц: '{selected_material}'")
        print(
            f"Остаток: {available_quantity} -> "
            f"{warehouse_data[selected_material]['quantity']}"
        )
    else:
        print("Недостаточно материала на складе")
else:
    print("Материал не найден")
