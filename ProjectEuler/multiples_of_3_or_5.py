sum: int = 0
for i in range(1, 1000, 1):

    if (i % 3 == 0) or (i % 5 == 0):
        sum += i
print(sum)
