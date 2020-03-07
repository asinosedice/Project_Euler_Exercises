import sys

longest = 0
winner = 0
for n in range(10000, 1000001):
    counter = 1
    i = n
    while i != 1:
        if i % 2 == 0:
            i = int(i/2)
        else:
            i = int(3*i+1)
        counter += 1
        if counter > longest:
            longest = counter
            winner = n
    print("if we start the sequence with the number " +
          str(n) + " we found " + str(counter) + " terms")
print("the number " + str(winner) +
      "have the longest chain of terms, with " + str(longest) + " terms.")
