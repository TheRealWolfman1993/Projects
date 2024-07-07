immutable_var = 1, 2, 3, "Четыре", "Пять", False
print(immutable_var)
print(type(immutable_var))

mutable_list = ["Первый", "Второй", "Третий", "Четвертый", "Пятый"]
print(type(mutable_list))
mutable_list[0] = "Десятый"
mutable_list[1] = "Девятый"
mutable_list[2] = "Восьмой"
mutable_list[3] = "Седьмой"
mutable_list[4] = "Шестой"
print(mutable_list)

immutable_var[0] = 1
immutable_var[1] = 1
immutable_var[2] = 1