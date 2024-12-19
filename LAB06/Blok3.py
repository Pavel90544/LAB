def longest_n_sequence_and_replace_exclamation(input_string):
    # Переменные для хранения самой длинной последовательности "н"
    max_count = 0
    current_count = 0
   
    # Обходим строку символ за символом
    for char in input_string:
        if char == 'н':
            current_count += 1  # Увеличиваем счетчик, если символ "н"
        else:
            if current_count > max_count:
                max_count = current_count  # Обновляем максимальное значение
            current_count = 0  # Сбрасываем счетчик

    # В случае, если строка заканчивается последовательностью "н"
    if current_count > max_count:
        max_count = current_count

    # Заменяем восклицательные знаки на точки
    transformed_string = input_string.replace('!', '.')

    print(f"Самая длинная последовательность 'н': {max_count}")
    print(f"Преобразованная строка: {transformed_string}")

