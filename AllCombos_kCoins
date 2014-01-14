#All possible combinations of k coins

def collapse(nested_list):
    new_list = []
    for list in nested_list:
        new_list = new_list + list
    return new_list

def how_many(n, list):
    count = 0
    for i in list:
        if i == n:
            count = count + 1
    return count
#--------------------------------
#overcounts by continuously squaring the sets of coins

def combos_1 (coins, k):
    count = 1
    while count < k:
        new_coins = []
        while len(coins) != 0:
            list = [coins[0]]*len(coins)
            inside_list = []
            for i in range(0,len(coins)):
                inside_list.append(list[i] + coins[i])
            new_coins.append(inside_list)
            coins.remove(coins[0])
        coins = collapse(new_coins)
        count = count + 1
    return coins

#--------------------------------
#double counts combinations with different permutations

def combos_2(coins, k):
    count = 1
    coins2 = [] + coins
    while count < k:
        coins1 = [] + coins
        nested_coins = []
        while len(coins1) != 0:
            list = [coins1[0]]*len(coins2)
            inside_list = []
            for i in range(0,len(coins2)):
                #if list[i]+coins2[i] <= 200:
                    inside_list.append(list[i] + coins2[i])
            nested_coins.append(inside_list)
            a=coins1[0]
            coins1.remove(a)
            coins2.remove(a)
        coins2 = collapse(nested_coins)
        count = count + 1
    return coins2

#-------------------------------

def distribute(num, list):
    for i in range(0, len(list)):
        list[i] = list[i] + num
    return list

#c1: ascedning, includes 0, distinct elements
#c2: ascending, includes 0, length >= length of c1
#c3: elements belong to c1, length = length of c2
def loop(c1, c2, c3):
    c2_new = []
    c3_new = []
    for i in range(0, len(c2)):
        for j in range(0, len(c1)):
            if c3[i] == c1[j]:
                c2_new.append(distribute(c2[i], c1[j:]))
                c3_new.append(c1[j:])
    c2 = collapse(c2_new)
    c3 = collapse(c3_new)
    return [c2,c3]

def combos(coins, k):
    count = 1
    coins1 = [] + coins
    coins2 = [] + coins
    while count < k:
        list = loop(coins, coins1, coins2)
        coins1 = list[0]
        coins2 = list[1]
        count = count + 1
    return coins1

#------------------------------
#test
print combos_1([0,1,2], 3)
print combos_2([0,1,2], 3)
print combos([0,1,2], 3)
