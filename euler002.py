import sys
numbers = [1, 2]
i = 3
j = 2

while i < 4000000:
    i = numbers[j-1] + numbers[j-2]
    numbers.append(i)
    j = j+1
total = 0

for number in numbers:
    if number % 2 == 0:
        total = total + number
print(total)
