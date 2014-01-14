#4 Largest palidrome product
import math
i = 100
answer = 1
while i < 1000:
    for j in range(100,1000):
        prod = i*j
        s = str(prod)
        first_half = s[:len(s)/2]
        second_half = s[int(math.ceil(len(s)/2.)):]
        if first_half == second_half[::-1]:
            if prod > answer:
                answer = prod
    i = i + 1
print answer
