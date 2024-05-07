with open('input.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file]

# Сортировка чисел по возрастанию цифр
sorted_numbers = sorted(numbers, key=str)

with open('output.txt', 'w') as file:
    for number in sorted_numbers:
        file.write(str(number) + '\n')