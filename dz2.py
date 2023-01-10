n = input('Введите целое число: ')
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print('Число не целое!')
        n = input('Введите целое число:')

if n % 2 == 0:
    print('Четное')
else:
    print('Нечетное')
