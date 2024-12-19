Number 1
def analyze_array():
    # Вводим массив из 10 целых чисел
    array = []
    for i in range(10):
        num = int(input(f"Введите целое число {i + 1}: "))
        array.append(num)

    # Находим максимальный элемент
    max_element = max(array)
   
    # Считаем количество меньших и больших максимального элемента
    count_less = sum(1 for x in array if x < max_element)
    count_greater = sum(1 for x in array if x > max_element)

    print(f"Максимальный элемент: {max_element}")
    print(f"Количество элементов меньше максимального: {count_less}")
    print(f"Количество элементов больше максимального: {count_greater}")

# Вызов функции
analyze_array()

Number 2
def sum_greater_than_five():
    # Вводим массив из 10 целых чисел
    array = []
    for i in range(10):
        num = int(input(f"Введите целое число {i + 1}: "))
        array.append(num)

    # Вычисляем сумму чисел, которые больше 5
    total_sum = sum(x for x in array if x > 5)

    print(f"Сумма чисел, которые больше 5: {total_sum}")

# Вызов функции
sum_greater_than_five()
