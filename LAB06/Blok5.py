Задача 1
def gcd(a, b):
    """Функция для нахождения НОД (Наибольший Общий Делитель) с использованием алгоритма Евклида."""
    while b:
        a, b = b, a % b
    return a

def subtract_fractions(A, B, C, D):
    """Функция для вычитания дробей A/B - C/D и возвращения несократимой дроби."""
    # Находим общий знаменатель
    common_denominator = B * D
    # Приводим дроби к общему знаменателю
    new_A = A * D
    new_C = C * B
    # Вычитаем дроби
    result_numerator = new_A - new_C
   
    # Сокращаем дробь
    if result_numerator == 0:
        return (0, 1)  # Если результат 0, возвращаем 0/1
    elif result_numerator < 0:
        result_numerator = -result_numerator  # Делаем числитель положительным
   
    divisor = gcd(result_numerator, common_denominator)
   
    return (result_numerator // divisor, common_denominator // divisor)

# Ввод данных
A = int(input("Введите числитель первой дроби (A): "))
B = int(input("Введите знаменатель первой дроби (B): "))
C = int(input("Введите числитель второй дроби (C): "))
D = int(input("Введите знаменатель второй дроби (D): "))

# Вычисляем результат
numerator, denominator = subtract_fractions(A, B, C, D)

# Вывод результата
print(f"Результат вычитания дробей: {numerator}/{denominator}")
Задача 2
def decimal_to_binary(n):
    """Рекурсивная функция для перевода числа из десятичной системы в двоичную."""
    if n == 0:
        return ""
    else:
        return decimal_to_binary(n // 2) + str(n % 2)

# Ввод числа
number = int(input("Введите целое число для перевода в двоичную систему: "))

# Обработка случая, когда число равно 0
if number == 0:
    binary_representation = "0"
else:
    binary_representation = decimal_to_binary(number)

# Вывод результата
print(f"Двоичное представление числа {number}: {binary_representation}")
