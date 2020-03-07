import sys
numbers = []

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        numbers.append(i)
total = 0
for i in numbers:
    total = total+i
print(total)
