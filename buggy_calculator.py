# Калькулятор с ошибками (для демонстрации Issues)

def add(a, b):
    return a + b  # Работает правильно

def subtract(a, b):
    return a - b  # Работает правильно

def multiply(a, b):
    return a * b  # Работает правильно

def divide(a, b):
    return a / b  # ОШИБКА: нет проверки деления на ноль!

def power(a, b):
    return a ** b  # Работает правильно

def mod(a, b):
    return a % b  # ОШИБКА: нет проверки деления на ноль!

def calculate():
    print("Простой калькулятор v1.0")
    print("1. Сложение")
    print("2. Вычитание") 
    print("3. Умножение")
    print("4. Деление")  # ОШИБКА: не обрабатывает деление на ноль
    
    choice = input("Выберите операцию: ")
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    
    if choice == "1":
        print(f"Результат: {add(a, b)}")
    elif choice == "2":
        print(f"Результат: {subtract(a, b)}")
    elif choice == "3":
        print(f"Результат: {multiply(a, b)}")
    elif choice == "4":
        print(f"Результат: {divide(a, b)}")  # Упадет при делении на ноль
    else:
        print("Неверный выбор")

if __name__ == "__main__":
    calculate()
