#46 Goldbach's other conjecture

import math

def is_square(int):
    sqrt = math.sqrt(int)
    if str(sqrt)[-2:] == '.0':
        return True
    else:
        return False

#returns a list of all primes smaller than the integer n
def find_primes(n):
    list_primes = []
    prime = 1
    number = prime + 1
    while prime < n:

        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                number = number + 1
                break
        else:
            prime = number
            list_primes.append(prime)
            number = number + 1
    list_primes.remove(list_primes[len(list_primes)-1])
    return list_primes


odd_comp = 1
number = odd_comp + 1
done = False
while 1:
    if done == True:
        break
    for i in range(2, int(math.sqrt(number)) + 1):
        if done == True:
            break
        elif number % i == 0 and number % 2 !=0:
            odd_comp = number
            for i in find_primes(odd_comp):
                if (odd_comp-i) % 2 == 0:
                    if is_square((odd_comp-i)/2):
                        #print odd_comp, i, (odd_comp-i)/2
                        number = number + 1
                        break
            else:
                print odd_comp
                done = True
                break
    else:
        number = number + 1
