from random import choice

# Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map((lambda ch_f, ch_s: True if ch_f == ch_s else False), first, second)))

# Замыкание:
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            file.writelines(map(lambda line: str(line) + '\n', data_set))
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Метод __call__:
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self, *args, **kwargs):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())