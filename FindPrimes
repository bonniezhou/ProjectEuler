import math

#divide by every number less than sqrt
prime = 1
number = prime + 1
while prime < 50:
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            number = number + 1
            break
    else:
        prime = number
        number = number + 1
        #print prime


#divide by every prime less than sqrt, given list_primes contains every prime less than sqrt
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

def is_prime(number):
    list_primes = find_primes(int(math.sqrt(number)))
    for i in list_primes:
        if number % i == 0:
            return False
    else:
        return True


# traverse list of every prime less than sqrt only once
def is_prime2(anumber):
    n = int(math.sqrt(anumber))
    prime = 1
    number = prime + 1
    list_primes =[]
    while prime < n:
        for i in list_primes:
            if i > int(math.sqrt(number)):
                prime = number
                if anumber % prime == 0:
                    return False
                list_primes.append(prime)
                number = number + 1
                break
            elif number % i == 0:
                number = number + 1
                break
        else:
            prime = number
            if anumber % prime == 0:
                    return False
            list_primes.append(prime)
            number = number + 1
    return True
