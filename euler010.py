import sys
import math


def isPrime(number):
    if number == 1:
        return False
    elif number < 4:
        return True
    elif number % 2 == 0:
        return False
    elif number < 9:
        return True
    elif number % 3 == 0:
        return False
    else:
        r = round(math.sqrt(number))
        f = 5
        while f <= r:
            if number % f == 0:
                return False
            if number % (f+2) == 0:
                return False
            f += 6
        return True


sum = 0
target = 2000000
seed = 1

while seed < target:
    if isPrime(seed) == True:
        sum += seed
        print("for primes below " + str(seed + 1) + "the sum equals " + str(sum))
    seed += 1
