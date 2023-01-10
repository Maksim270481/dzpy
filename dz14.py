
## 1 var
# def func(a, b, c):
#     s = 0
#
#
#     def inner(x, y):
#         nonlocal s
#         s = x * y
#         return s
#
#     return 2 * (inner(a, b) + inner(b, c) + inner(a, c))
#
#
# print(func(2, 4, 6))
# print(func(8, 8, 2))
# print(func(1, 6, 8))



## 2 var
# s = 0
# def func(a, b, c):
#
#
#
#     def inner(x, y):
#         global s
#         s = x * y
#         return s
#
#     return 2 * (inner(a, b) + inner(b, c) + inner(a, c))
#
#
# print(func(2, 4, 6))
# print(func(8, 8, 2))
# print(func(1, 6, 8))




