# Работа со словарями

my_dict = {'Артём': 1991,
           'Алина': 1992,
           'Максим': 1993,
           'Полина': 1990,
           'Анна': 1989}
print("Dictionary:", my_dict)
print("Existing value:", my_dict['Артём'])
print("Not existing value:", my_dict.update({'Антон': 1985}))
del my_dict['Алина']
print
print("Modified dictionary:", my_dict)
print()

# Работа с множествами

my_set = {1, 1, 4.5, 4.5, True, True, False, 'Раз', 'Раз', 'Два', 'Два'}
print("Set:", my_set)
my_set.add(7)
my_set.add(8)
my_set.remove(1)
print("Modified set:", my_set)