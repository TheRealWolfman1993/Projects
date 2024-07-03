immutable_var = 1, 2, 3, "Четыре", "Пять", False
print(immutable_var)

# immutable_var[0][0] = 1
# print(immutable_var)

mutable_list = ["Первый", "Второй", "Третий", "Четвертый", "Пятый"]
mutable_list[0] = "Десятый"
mutable_list[1] = "Девятый"
mutable_list[2] = "Восьмой"
mutable_list[3] = "Седьмой"
mutable_list[4] = "Шестой"
print(mutable_list)
