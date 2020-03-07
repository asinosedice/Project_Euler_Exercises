import sys
divisors = 0
start = 10000


def factorize(n):
    total = 0
    for i in range(1, n+1):
        if n % i == 0:
            total += 1
    return total


while divisors < 501:
    triangleNumber = 0
    start += 1

    for i in range(1, start):
        triangleNumber += i
    divisors = factorize(triangleNumber)
    print("the number " + str(triangleNumber) +
          " has " + str(divisors) + " divisors.")
