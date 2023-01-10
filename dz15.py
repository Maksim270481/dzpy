lst = [int(input('->')) for i in range(int(input('Введите колво значений: ')))]


def fuc(rur):
    s = 0
    for i in lst:
        s += i
    print(s)
    print(rur())


@fuc
def funcy():
    k = 0
    ch = 0
    for i in lst:
        k += 1
        ch = ch + i
    return ch/k

