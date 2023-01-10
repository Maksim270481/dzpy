a = [int(input("-> ")) for i in range(int(input("Количество элементов: ")))]
for i in range(len(a)):
    if a[(i-1)] < a[i]:
        print(a[i])
    i +=1