def print_params(a=1, b='Строка', c=True):
    print(a, b, c)

values_list = [True, int(4), 'Wolf']
values_dict = {'a': 'Wolf', 'b': 25, 'c': False}

print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [int(4), 'Wolf']
print_params(*values_list_2, 42)