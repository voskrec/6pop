#егор
def count_letters(text):
    vowels = "аеёиоуыэюяaeiouy" # Русские и английские гласные
    consonants = "бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxz" # Русские и англ. согласные
    
    v_count = 0
    c_count = 0
    
    # Приводим к нижнему регистру для удобства
    text_lower = text.lower()
    
    for char in text_lower:
        if char in vowels:
            v_count += 1
        elif char in consonants:
            c_count += 1
            
    return v_count, c_count

# Проверка
#ислам
my_list = [10, 5, 20, 20, 8, 15]
print(second(my_list))  # Выведет 15

=======
text = input("Введите текст: ")
v, c = count_letters(text)
print(f"Гласных: {v}, Согласных: {c}")
>>>>>>> origin/islam
