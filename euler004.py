import sys


def palindromeCheck(n):
    word = str(n)
    if list(word) == list(reversed(word)):
        return True
    else:
        return False


greater = 0
for i in range(1, 1000):
    for j in range(1, 1000):
        candidate = i*j
        if (palindromeCheck(candidate) == True) and candidate > greater:
            greater = candidate
print(greater)
