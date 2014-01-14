#1 Multiples of 3 and 5
i = 1
sum = 0
while i < 1000:
    if i % 3 == 0:
        sum = sum + i
        i = i + 1
    elif i % 5 == 0:
        sum = sum + i
        i = i + 1
    else:
        i = i + 1
print sum
#------------------------------
#1 Multiples of 3 and 5 *hint from Wikipedia
sum_three = 3*333*334/2.
sum_five = 5*199*200/2.
sum_fifteen = 15*66*67/2.
sum_total = sum_three + sum_five - sum_fifteen
print sum_total
