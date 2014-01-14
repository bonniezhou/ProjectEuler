import math
def isprime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    else:
        return True

prime = 1
n = 1
while n < 1000000:
    prime = prime + 1
    while isprime(prime) == False:
        prime = prime + 1
    n = n*prime
print n/prime
