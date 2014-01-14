#95

#another approach for propDivisors: generate prime factorization and all possible combinations of prime factors
def sumPropDivisors(n):
    factor = 1
    listFactors = []
    sum = 0
    while factor < n:
        if n % factor == 0:
            listFactors.append(factor)
            sum = sum + factor
        factor = factor + 1
    return sum

def isPerfect(n):
    if n == sumPropDivisors(n):
        return True
    else:
        return False

def amiChain(num):
    chainCount = 1
    chain = [num]
    while num < 1000000:
        num = sumPropDivisors(num)
        if isPerfect(num) == True:
            return False
        if num == chain[0]:
            return chain
        elif num in chain:
            return False
        chainCount = chainCount + 1
        chain.append(num)
    return False

number = 12496
longest = 0
past = []
while number < 1000000:
    if number not in past:
        if amiChain(number) != False:
            currentChain = amiChain(number)
            print currentChain
            for n in currentChain:
                past.append(n)
            if len(currentChain) > longest:
                longest = len(currentChain)
                longestChain = currentChain
    number = number + 1
print longestChain
