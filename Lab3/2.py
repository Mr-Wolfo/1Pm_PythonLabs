str = input("")
str2 = ""
n = ""
i = 0

#Any number
while i < len(str):
    temp = i

    while str[temp].isdigit():
        n += str[temp]
        if temp == len(str)-1:
            break
        else:
            temp += 1

    if n != "":
        print(n)
        str2 += str[i-1] * (int(n)-1)
        i += len(n)-1
        n = ""
    else:
        str2 += str[i]
    i += 1

print(str2)
