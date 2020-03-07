import sys
k = 1
j = 100

flag = False
while flag == False:
    for i in range(2, 21):
        if j % i == 0:
            k += 1
    if k == 20:
        flag = True
    else:
        j += 1
        k = 1
print(j)
