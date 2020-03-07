import sys

target = 600851475143
for i in range(target, 0, -1):
    if target % i == 0:
        print(i)
