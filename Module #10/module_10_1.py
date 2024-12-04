# Импорты необходимых модулей и функций
from threading import Thread
from datetime import datetime
from time import sleep

# Объявление функции write_words
def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(1, word_count+1):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')

# Взятие текущего времени
time_start = datetime.now()

# Запуск функций с аргументами из задачи
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# Взятие текущего времени
time_end = datetime.now()

# Вывод разницы начала и конца работы функций
print(f'Работа потоков {time_end - time_start}')

# Взятие текущего времени
time_start = datetime.now()

# Создание и запуск потоков с аргументами из задачи
th1 = Thread(target=write_words, args=(10, 'example5.txt'))
th2 = Thread(target=write_words, args=(30, 'example6.txt'))
th3 = Thread(target=write_words, args=(200, 'example7.txt'))
th4 = Thread(target=write_words, args=(100, 'example8.txt'))

th1.start()
th2.start()
th3.start()
th4.start()

th1.join()
th2.join()
th3.join()
th4.join()

# Взятие текущего времени
time_end = datetime.now()

# Вывод разницы начала и конца работы потоков
print(f'Работа потоков {time_end - time_start}')
