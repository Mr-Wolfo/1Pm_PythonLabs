n = int(input("Кол-во городов: "))
S = []

for i in range(n):
    temp = input("Введите город: ")
    if temp not in S:
        print("OK")
        S.append(temp)
    else:
        print("REPEAT")
