def factorial(k):
    factorial = 1
    if k != 0:
        for i in range(1,k+1):
            factorial = factorial*i
    return factorial

def choose(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))

count = 0
for n in range(1,101):
    for r in range(1, n/2 + 1):
        if choose(n,r) > 1000000:
            if r == n/2.:
                count = count + 1
            else:
                count = count + 2
print count
