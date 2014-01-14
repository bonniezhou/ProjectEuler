#35
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


num = 2
circulars = []
while num < 500000: #finds all circular primes under 1 million
    if num not in circulars:
        if is_prime(num) == True:
            iterations = len(str(num))-1
            rotations = [num]
            rotate = num
            while iterations > 0:
                if str(rotate)[1]=='0':
                    break
                rotate = int(str(rotate)[1:]+str(rotate)[0])
                if is_prime(rotate) == False:
                    break
                rotations.append(rotate)
                iterations = iterations-1
            #add code here to remove duplication of the number 11
            if iterations == 0:
                for n in rotations:
                    circulars.append(n)
    num = num + 1
print circulars
print len(circulars)
        
#number 11 is duplicated
