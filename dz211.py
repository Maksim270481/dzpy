def perevodCh(a):
    b = ''
    while a > 0:
        b = b + str(a % 2)
        a = a // 2
    return b[::-1]


print(perevodCh(53))
print(perevodCh(145))
print(perevodCh(255))
print(perevodCh(0))
