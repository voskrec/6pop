<<<<<<< HEAD\
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
print(most_frequent(my_list))  # Выведет 1

#islam
import re

def remove_html_tags(text):
    # Регулярное выражение: <.*?> 
    # <  - начало тега
    # .* - любые символы
    # ?  - не жадный поиск (останавливается на первом закрывающем >)
    # >  - конец тега
    clean_text = re.sub(r'<.*?>', '', text)
    
    # Убираем лишние пробелы, которые могли образоваться после удаления тегов
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    
    return clean_text

# Тестирование
if __name__ == "__main__":
    html_text = "<h1>Привет, мир!</h1><p>Это <b>тестовый</b> текст с <a href='#'>ссылкой</a>.</p>"
    print("Исходный текст:")
    print(html_text)
    print("\nТекст без HTML-тегов:")
    print(remove_html_tags(html_text))
>>>>>>> origin/islam
