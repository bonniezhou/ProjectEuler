import math

max = 9901

def is_perm(num1, num2):
    list1 = list(str(num1))
    list2 = list(str(num2))
    for i in list1:
        if i in list2:
            list2.remove(i)
        else:
            return False
    return True


list_primes =[]
prime = 1000
number = prime + 1
while prime < max:
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            number = number + 1
            break
    else:
        prime = number
        number = number + 1
        list_primes.append(prime)
list_primes.remove(list_primes[len(list_primes)-1])


list_perms = []
list_primes2 = [] + list_primes
for n1 in list_primes:
    list_primes2.remove(n1)
    for n2 in list_primes2:
        if is_perm(n1,n2) == True:
            if n1 not in list_perms:
                list_perms = list_perms + [n1,n2]
            elif n2 not in list_perms:
                list_perms.append(n2)

#Note: all_perms crashes when max is set to > 9901. 9901 is the last element in list_perms.
all_perms = []
while len(list_perms) > 2:
    permlist =[]
    while is_perm(list_perms[0], list_perms[1]) == True:
        permlist.append(list_perms[1])
        list_perms.remove(list_perms[1])
    permlist.insert(0, list_perms[0])
    list_perms.remove(list_perms[0])
    all_perms.append(permlist)

if is_perm(list_perms[0],all_perms[len(all_perms)-1][0]) == True:
    all_perms[len(all_perms)-1].append(list_perms[0])
    all_perms[len(all_perms)-1].append(list_perms[1])
else:
    all_perms.append(list_perms)

#---------------------------------------
#trying to find differences - complicated
##def list_sum(list):
##    sum = 0
##    for i in list:
##        sum = sum + i
##    return sum
##
##for perm in all_perms:
##    if len(perm) >= 3:
##        diffs = []
##        for i in range(1, len(perm)):
##            diff = perm[i]-perm[i-1]
##            diffs.append(diff)
##
##        #print diffs
##        for h in range(0, len(diffs)):
##            for i in range(h+1, len(diffs)):
##                sum1 = list_sum(diffs[h:i])
##                for j in range(i+1, len(diffs)):
##                    sum2 = list_sum(diffs[i:j])
##                    if sum1 == sum2:
##                        print sum1
##                        print perm[h], perm[i], perm[j]
##
#----------------------------------------
for perm in all_perms:
    if len(perm) >= 3:
        for h in range(0, len(perm)):
            for i in range(h+1, len(perm)):
                diff1 = perm[i]-perm[h]
                for j in range(i+1, len(perm)):
                    diff2 = perm[j]-perm[i]
                    if diff1 == diff2:
                        print diff1
                        print perm
            
