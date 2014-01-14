#2 Even Fibonacci numbers
i = 1
j = 2
sum = 0
while j < 4000000:
    k = i+j
    if k % 2 == 0:
        sum = sum + k
        i = j
        j = k
    else:
        i = j
        j = k
print sum + 2

