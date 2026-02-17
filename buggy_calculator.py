def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b

def power(a, b):
    return a ** b

def mod(a, b):
    if b == 0:
        return "Ошибка: деление на ноль!"
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
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: введите числа!")
        return
    
    if choice == "1":
        print(f"Результат: {add(a, b)}")
    elif choice == "2":
        print(f"Результат: {subtract(a, b)}")
    elif choice == "3":
        print(f"Результат: {multiply(a, b)}")
    elif choice == "4":
        print(f"Результат: {divide(a, b)}")
    elif choice == "5":
        print(f"Результат: {power(a, b)}")
    elif choice == "6":
        print(f"Результат: {mod(a, b)}")
    else:
        print("Неверный выбор")

if __name__ == "__main__":
    calculate()