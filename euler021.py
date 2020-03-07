def properDivisorsSum(n):
    properDivisors = []
    sum = 0
    if n % 2 == 0:
        endTerm = int((n/2)+1)
    else:
        endTerm = int(((n+1)/2))
    for i in range(1, endTerm):
        if n % i == 0:
            properDivisors.append(i)
    for i in properDivisors:
        sum += i
    return sum


def isAmicable(m):
    first = properDivisorsSum(m)
    second = properDivisorsSum(first)
    if second == m:
        return first
    else:
        return False


sumOfAmicables = 0
amicables = []
for i in range(10, 10000):
    if i not in amicables:
        if isAmicable(i) != False and i != isAmicable(i):
            amicables.append(i)
            amicables.append(isAmicable(i))

print(str(sum(amicables)))
