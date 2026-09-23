# Задание 1.2 - Конвертер единиц измерения расстояния

# Коэффициенты перевода выбранной единицы в метры
TO_METERS = {
    "1": ("км", 1000.0),
    "2": ("м",  1.0),
    "3": ("см", 0.01),
    "4": ("мм", 0.001),
    "5": ("mi", 1609.344),
    "6": ("yd", 0.9144),
}


def is_number(text):
    # Строка считается числом, если после отбрасывания знака
    # и одной десятичной точки в ней остаются только цифры
    text = text.strip().replace(",", ".")
    if text.startswith("-") or text.startswith("+"):
        text = text[1:]
    return text.replace(".", "", 1).isdecimal()


print("Конвертер единиц измерения расстояния")
print("1 - Километры (км)")
print("2 - Метры (м)")
print("3 - Сантиметры (см)")
print("4 - Миллиметры (мм)")
print("5 - Мили (mi)")
print("6 - Ярды (yd)")

src = input("Выберите исходную единицу (1-6): ").strip()
dst = input("Выберите целевую единицу (1-6): ").strip()

if src not in TO_METERS:
    print("Ошибка: пункта «" + src + "» в меню нет.",
          "Введите номер исходной единицы - число от 1 до 6")
elif dst not in TO_METERS:
    print("Ошибка: пункта «" + dst + "» в меню нет.",
          "Введите номер целевой единицы - число от 1 до 6")
else:
    value_text = input("Введите значение для конвертации: ")
    if not is_number(value_text):
        print("Ошибка: «" + value_text + "» - это не число.",
              "Укажите значение цифрами, например 12 или 3.5")
    elif float(value_text.replace(",", ".")) < 0:
        print("Ошибка: расстояние не может быть отрицательным.",
              "Введите число, большее или равное нулю")
    else:
        value = float(value_text.replace(",", "."))
        src_name, src_k = TO_METERS[src]
        dst_name, dst_k = TO_METERS[dst]
        result = value * src_k / dst_k            # перевод через метры
        print(format(value, "g"), src_name, "=",
              format(result, ".4f"), dst_name)
