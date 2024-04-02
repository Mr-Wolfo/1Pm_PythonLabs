n = int(input("Кол-во записей: "))
A = {}

for i in range(n):
    id, production, count = input().split()
    A[id][production] = A.setdefault(id, {}).setdefault(production, 0) + int(count)
for j in A:
    print(f"Список покупателя с Id = {j}:")
    for i in A[j].items():
        print(*i)