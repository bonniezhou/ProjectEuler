import math

def is_prime(anumber):
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


four_primes = [3,7,109,673]
prime = 673
number = prime + 1

while True:
    if is_prime(number) == False:
        number = number + 1
    else:
        prime = number
        number = number + 1
        for p in four_primes:
            if is_prime(int(str(prime)+str(p))) == False:
                break
            elif is_prime(int(str(p)+str(prime))) == False:
                break
        else:
            print prime
            break
