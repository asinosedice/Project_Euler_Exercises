import sys

solution = 0
abc = []
a = 0
d = 0
solved = False
for c in range(997, 3, -1):
    d = c**2
    for b in range(1000-c-1, 2, -1):
        a = 1000-c-b
        if a == 0:
            break
        if d == (b**2)+(a**2):
            abc = [a, b, c]
            solution = a*b*c
            solved = True
            break
    if solved == True:
        break
print(abc)
print(solution)
