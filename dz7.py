lst = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
row = 0
for row in lst:
    for col in lst:
        print(col, end='\t')
    print()
print('-----------------------')
i = 0
for col in row:
    for row in lst:
        print(row[i], end='\t')
    i += 1
    print()