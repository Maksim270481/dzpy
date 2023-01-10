prod = {
    'Jhon': {'N': '3056', 'S': '8463', 'E': '8441', 'W': '2694'},
    'Tom': {'N': '4832', 'S': '6786', 'E': '4737', 'W': '3612'},
    'Anne': {'N': '5239', 'S': '4802', 'E': '5820', 'W': '1859'},
    'Fiona': {'N': '3904', 'S': '3645', 'E': '8821', 'W': '2451'},
}

for i in prod:
    print(i)
    print('N:', prod[i]['N'])
    print('s:', prod[i]['S'])
    print('E:', prod[i]['E'])
    print('W:', prod[i]['W'])
a = str(input('Имя:'))
b = str(input('Регион:'))
print(prod[a][b])
c = str(input('Новое значение: '))
prod[a][b] = c
print(prod[a])