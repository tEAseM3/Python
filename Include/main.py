import string

# Функція для сортування слів
def sort_words(words):
    # Поділ на українські та англійські слова
    uk_words = sorted([w for w in words if w[0].lower() in 'абвгґдежзийклмнопрстуфхцчшщьюяєії'])
    en_words = sorted([w for w in words if w[0].lower() not in 'абвгґдежзийклмнопрстуфхцчшщьюяєії'])
    return uk_words + en_words

try:
    # Зчитування файлу
    with open('text.txt', 'r', encoding='utf-8') as file:
        # Читання першого рядка
        first_line = file.readline().strip()
        print("Перше речення:", first_line)

        # Видалення знаків пунктуації та розбиття на слова
        words = first_line.translate(str.maketrans('', '', string.punctuation)).split()
        
        # Сортування слів
        sorted_words = sort_words(words)
        
        # Виведення відсортованих слів і їхньої кількості
        print("Відсортовані слова:", sorted_words)
        print("Кількість слів:", len(sorted_words))
except FileNotFoundError:
    print("Помилка: Файл не знайдено.")
except Exception as e:
    print("Сталася помилка:", e)
