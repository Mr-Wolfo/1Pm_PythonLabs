A = [i for i in input("Введите текст: ").split(" ")]

D = dict()
for i in A:
    D[i] = D.get(i, 0) + 1
    print(D[i] - 1, end=" ")
