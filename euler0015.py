# solved by combinatary (thanks Xavier)


def factorial(n):
    result = 1
    for i in range(n, 0, -1):
        result *= i
    return result


answer = factorial(40)/(factorial(20)**2)
print(answer)
