products = {                           # словник із товарами та їх цінами
    "яблуко": 12.00,
    "банан": 25.50,
    "апельсин": 30.00,
    "кавун": 80.00
}

def format_price(price):# функція форматування ціни
    return f"ціна: {price:.2f} грн"# повертає ціну з двома знаками після коми
def check_availability(*items):# функція перевіряє наявність товарів
    available = {}# створюємо словник для збереження результатів
    for item in items:# перевіряємо кожен товар
        if item in products:
            available[item] = True# товар є
        else:
            available[item] = False# товару немає
    return available# повертаємо результат перевірки
def make_order():# основна функція оформлення замовлення
    cart = input("Введіть товари через кому: ").split(",")# вводимо список товарів
    cart = [item.strip().lower() for item in cart]# прибираємо пробіли та вирівнюємо регістр
    availability = check_availability(*cart)# перевіряємо, чи всі товари є в наявності
    if not all(availability.values()):# якщо хоча б одного товару немає
        print("Не всі товари є в наявності:")
        for item, is_available in availability.items():
            if not is_available:
                print(f" - {item} немає в магазині")# показуємо відсутні товари
        return# зупиняємо оформлення
    total = sum(products[item] for item in cart)# рахуємо загальну вартість
    print(f"Усі товари є в наявності. Загальна {format_price(total)}")# виводимо суму
    action = input("Введіть 'купити' або 'переглянути ціну': ").lower()# запитуємо дію користувача
    if action == "купити":# якщо користувач обрав купити
        print("Дякуємо за покупку!")
    elif action == "переглянути ціну":# якщо хоче переглянути ціни
        for item in cart:
            print(f"{item}: {format_price(products[item])}")# виводимо ціну кожного товару
    else:
        print("Невідома команда.")# якщо команда невірна

def main():
    process_order()


if __name__ == '__main__':
    main()
