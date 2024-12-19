# Задача 1: Средняя оценка по физике
def average_grade():
    grades = []
    # Заполняем список оценок
    for i in range(20):
        while True:
            try:
                grade = float(input(f"Введите оценку для ученика {i + 1}: "))
                if 0 <= grade <= 100:  # Предположим, что оценки в диапазоне от 0 до 100
                    grades.append(grade)
                    break
                else:
                    print("Ошибка: Оценка должна быть в диапазоне от 0 до 100.")
            except ValueError:
                print("Ошибка: Пожалуйста, введите действительное число.")

    # Вычисляем среднюю оценку
    average = sum(grades) / len(grades)
    print(f"Средняя оценка по физике: {average:.2f}")

average_grade()

# Задача 2: Наибольшее целое число K
def largest_k_less_than_a():
    A = float(input("Введите число A (> 1): "))
   
    if A <= 1:
        print("Ошибка: A должно быть больше 1.")
        return
   
    K = 0
    total_sum = 0.0

    while True:
        K += 1
        total_sum += 1 / K
       
        if total_sum >= A:
            K -= 1  # Уменьшаем K на 1, так как последняя итерация привела к превышению A
            total_sum -= 1 / K  # Соответственно, убираем последний добавленный элемент
            break

    print(f"Наибольшее целое число K: {K}")
    print(f"Сумма 1 + 1/2 + ... + 1/{K}: {total_sum:.6f}")

largest_k_less_than_a()
