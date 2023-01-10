# sl1 = {1: 10, 2: 20}
# sl2 = {3: 30, 4: 40}
# sl3 = {5: 50, 6: 60}
# print({**sl1, **sl2, **sl3})


# dansl = {
#     'emp1': {'name': 'Jhon', 'salary': '7500'},
#     'emp2': {'name': 'Emma', 'salary': '8000'},
#     'emp3': {'name': 'Brad', 'salary': '6500'}
# }
# print(dansl['emp3'])
# dansl['emp3']['salary'] = '8500'
# print('emp1')
# print('name: ', dansl['emp1']['name'])
# print('salary: ', dansl['emp1']['salary'])
# print('emp2')
# print('name: ', dansl['emp2']['name'])
# print('salary: ', dansl['emp2']['salary'])
# print('emp3')
# print('name: ', dansl['emp3']['name'])
# print('salary: ', dansl['emp3']['salary'])

# n = int(input('Кол-во студентов: '))
# stud = {}
# s = 0
# for i in range(n):
#     lastname = input(str(i + 1) + '-й студент')
#     mark = int(input('Балл: '))
#     stud[lastname] = mark
#     s += mark
# avrg = s / n
# print('Средний балл: ', round(avrg, 1))
# print('Студенты с баллом выше среднего: ')
# for i in stud:
#     if stud[i] > avrg:
#         print(i)
