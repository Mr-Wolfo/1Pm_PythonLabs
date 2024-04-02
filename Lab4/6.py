A = [i for i in input("Введите текст: ").split(" ")]
D = dict()

for i in range(len(A)):
    D[A[i]] = D.setdefault(A[i], 0) + 1
X = sorted(D.items(), key = lambda item: (item[1], item[0]), reverse = True)
for i in X:
    print(*i)