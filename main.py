#egor
from collections import Counter

def most_frequent(nums):
    if not nums:
        return None
    # Counter считает частоту каждого элемента
    # most_common(1) возвращает список из одного кортежа:
    return Counter(nums).most_common(1)[0][0]

# Проверка
my_list = [1, 3, 3, 2, 1, 3, 4, 1]
print(most_frequent(my_list))  # Выведет 3 

