print('Вычисляем средний бал')
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
Sort_grades = (sum(grades[0])/len(grades[0]),
               sum(grades[1])/len(grades[1]),
               sum(grades[2])/len(grades[2]),
               sum(grades[3])/len(grades[3]),
               sum(grades[4])/len(grades[4]))
print(Sort_grades)
print('Cортируем учеников')
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
Sort_name = sorted(students)
print(Sort_name)
print('Формируем словарь')
Dict_result = {Sort_name[0]: Sort_grades[0],
               Sort_name[1]: Sort_grades[1],
               Sort_name[2]: Sort_grades[2],
               Sort_name[3]: Sort_grades[3],
               Sort_name[4]: Sort_grades[4]}
print(Dict_result)