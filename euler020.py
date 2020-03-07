def factorial(n):
    result=1
    for i in range(n,0,-1):
        result*=i
    return result

sum=0
factorial=str(factorial(100))
for i in factorial:
    sum+=int(i)

print(factorial)
print(sum)    