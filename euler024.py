def normalize(n):
    if n > 2:
        normalized = (-3)+n
        return normalized
    else:
        return n


count = 1
elements = [0, 1, 2]
total = 3
for a in range(total):
    for b in range(a+1, total+1):
        for c in range(b+1, total+2):
            thisOne = [elements[a],
                       elements[normalize(b)], elements[normalize(c)]]
            print(str(thisOne))
            count += 1
