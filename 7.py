#7 10001st prime
import math
count = 3
prime = 5
number = prime + 1
while count < 10001:
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            number = number + 1
            break
    else:
        prime = number
        count = count + 1
        number = number + 1
print count
print prime
