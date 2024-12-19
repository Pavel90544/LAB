import math

def get_numbers(count):
    numbers = []
    while len(numbers) < count:
        try:
            num = float(input(f"Введите число {len(numbers) + 1}: "))
            numbers.append(num)
        except ValueError:
            print("Ошибка: Пожалуйста, введите действительное число.")
    return numbers

def main():
    print("Введите 4 числа для вычисления косинуса минимального из них.")
    numbers = get_numbers(4)

    # Находим минимальное число
    min_number = min(numbers)

    # Вычисляем косинус минимального числа
    cos_min_number = math.cos(min_number)

    # Выводим результат
    print("Минимальное число:", min_number)
    print("Косинус минимального числа:", cos_min_number)

if __name__ == "__main__":
    main()


