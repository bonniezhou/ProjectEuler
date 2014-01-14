#146
#not efficient

import math
def find_primes(n):
    prime = 1
    number = prime + 1
    list_primes =[]
    while prime < n:
        for i in list_primes:
            if i > int(math.sqrt(number)):
                prime = number
                list_primes.append(prime)
                number = number + 1
                break
            elif number % i == 0:
                number = number + 1
                break
        else:
            prime = number
            list_primes.append(prime)
            number = number + 1
    return list_primes

def pattern(n):
    if n % 2 == 0:
        primes = find_primes(n*n+27)
        last = len(primes)-1
        sqr=n*n
        if primes[last] == sqr+27 and primes[last-1] == sqr+13 and primes[last-2] == sqr+9 and primes[last-3] == sqr+7 and primes[last-4] == sqr+3 and primes[last-5] == sqr+1:
                return True
    return False
    

n = 1
sum = 0
while n < 1000:
    if pattern(n) == True:
        sum = sum + n
    print n
    n=n+1
print sum
