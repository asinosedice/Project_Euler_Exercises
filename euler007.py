import sys
primes = [2]
suspect = 3
while len(primes) < 10001:
    isPrime = True
    toPrint = False
    for i in primes:
        if suspect % i == 0:
            isPrime = False
            break
    if isPrime == True:
        primes.append(suspect)
        print("el número " + str(suspect) +
              " es el primo numero " + str(len(primes)))
    suspect += 1
