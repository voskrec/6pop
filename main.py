def second(num):
    # Убираем дубликаты, преобразуя в множество
    unique_nums = set(num)
    
    # Если уникальных чисел меньше 2, второго по величине нет
    if len(unique_nums) < 2:
        return None
        
    # Сортируем и берем предпоследний элемент
    return sorted(unique_nums)[-2]

# Проверка
my_list = [10, 5, 20, 20, 8, 15]
print(second(my_list))  # Выведет 15

