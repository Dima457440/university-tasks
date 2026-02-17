def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль!"  # Добавлен отступ (4 пробела)
    return a / b

def power(a, b):
    return a ** b

def mod(a, b):
    if b == 0:
        return "Ошибка: деление на ноль!"  # Добавлен отступ (4 пробела)
    return a % b

def calculate():
    print("Простой калькулятор v1.0")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Остаток от деления")

    choice = input("Выберите операцию: ")

    try:
        a = float(input("Введите первое число: "))  # Добавлен отступ
        b = float(input("Введите второе число: "))  # Добавлен отступ
    except ValueError:
        print("Ошибка: введите числа!")  # Добавлен отступ
        return

    if choice == "1":
        print(f"Результат: {add(a, b)}")  # Добавлен отступ
    elif choice == "2":
        print(f"Результат: {subtract(a, b)}")  # Добавлен отступ
    elif choice == "3":
        print(f"Результат: {multiply(a, b)}")  # Добавлен отступ
    elif choice == "4":
        print(f"Результат: {divide(a, b)}")  # Добавлен отступ
    elif choice == "5":
        print(f"Результат: {power(a, b)}")  # Добавлен отступ
    elif choice == "6":
        print(f"Результат: {mod(a, b)}")  # Добавлен отступ
    else:
        print("Ошибка: введите корректно!")  # Добавлен отступ

if __name__ == "__main__":
    calculate()