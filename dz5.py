sp = [int(input('->')) for i in range(int(input('Ввелите кол-во значений: ')))]
x = int(input('Введите число: '))
for i in range(len(sp)):
    if x == sp[i]:
        print('Это числo есть в списке.')
        break
else:
    print('Это чило не пренадлежит данному списку.')