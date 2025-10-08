grades = {}  # створюємо порожній словник для зберігання даних студентів

while True:
    name = input("Введіть ім'я студента (або 'stop' для завершення): ").strip()
    if name.lower() == "stop":
        break  # припиняємо цикл, якщо користувач ввів 'stop'

    try:
        grade = int(input(f"Введіть оцінку для {name}: "))
        if 1 <= grade <= 12:
            grades[name] = grade  # додаємо пару "ім'я: оцінка" у словник
        else:
            print("⚠️ Оцінка має бути від 1 до 12!")
    except ValueError:
        print("⚠️ Помилка: оцінка повинна бути числом!")
        continue  # пропускаємо ітерацію, якщо введено неправильне значення

# Виведення результатів
print("\nСписок студентів та їх оцінок:")
for name, grade in grades.items():
    print(f"{name}: {grade}")

# Якщо введено хоч одного студента — обчислюємо статистику
if grades:
    avg = sum(grades.values()) / len(grades)
    print(f"\nСередній бал по групі: {avg:.2f}")

    # Створюємо списки студентів за категоріями
    vidminnyky = [n for n, g in grades.items() if 10 <= g <= 12]
    khoroshysty = [n for n, g in grades.items() if 7 <= g <= 9]
    vidstayuchi = [n for n, g in grades.items() if 4 <= g <= 6]
    ne_sdaly = [n for n, g in grades.items() if 1 <= g <= 3]

    # Виводимо статистику по категоріях
    print(f"\nВідмінники (10–12): {len(vidminnyky)} -> {', '.join(vidminnyky) if vidminnyky else 'немає'}")
    print(f"Хорошисти (7–9): {len(khoroshysty)} -> {', '.join(khoroshysty) if khoroshysty else 'немає'}")
    print(f"Відстаючі (4–6): {len(vidstayuchi)} -> {', '.join(vidstayuchi) if vidstayuchi else 'немає'}")
    print(f"Не здали (1–3): {len(ne_sdaly)} -> {', '.join(ne_sdaly) if ne_sdaly else 'немає'}")
else:
    print("\nДані не введено.")
