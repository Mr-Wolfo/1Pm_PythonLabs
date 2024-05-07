with open('input.txt', 'r') as input_file:
    numbers = list(map(int, input_file.readline().split()))

prod = 1
for number in numbers:
    prod *= number

with open('output.txt', 'w') as output_file:
    output_file.write(str(prod))