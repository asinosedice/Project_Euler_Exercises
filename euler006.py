import sys


def squareOfSum(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum**2


def sumOfSquares(n):
    sum = 0
    for i in range(n+1):
        sum += i**2
    return sum


print(squareOfSum(100)-sumOfSquares(100))
