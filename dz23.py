# def func(n):
#     if len(n) == 0:
#         return 0
#     else:
#         res = func(n[1:])
#         if n[0] < 0:
#             res += 1
#         return res
#
#
# print('n =', func([-2, 3, 8, -11, -4, 6]))

names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bart', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']


def count(lst):
    cnt = 0
    for i in lst:
        if isinstance(i, list):
            cnt += count(i)
        else:
            cnt += 1
    return cnt


print(count(names))